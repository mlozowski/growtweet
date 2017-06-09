
import time

import tweepy

from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import twitter.data
from .auth import (
    redirect_to_twitter_auth,
    get_twitter_api,
)
from .models import (
    TwitterUser,
    Follower,
)


def limit_handled(cursor):
    """
    It handles Twitter data limitation. We have to wait for 15 minutes
    to another data delivery.
    :param cursor: tweepy.Cursor
    :return: Next data from response
    """
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            # it is very naive approach, but for such a limited time
            # it has to be enough
            time.sleep(16 * 60)


def twitter_login(request):
    return redirect_to_twitter_auth(request)


class Followers(View):
    template_name = 'twitter/followers.html'

    def get(self, request):
        verifier = request.GET.get('oauth_verifier', None)
        if verifier is not None:
            request.session['oauth_verifier'] = verifier
            return render(request, self.template_name, {'loading': True})
        else:
            return render(request, self.template_name, {'loading': False})


class GetRefreshedFollowers(APIView):

    def __init__(self, **kwargs):
        self.api = None
        super(GetRefreshedFollowers, self).__init__(**kwargs)

    def get(self, request):
        verifier = self.request.session['oauth_verifier']
        self.api = get_twitter_api(self.request, verifier)
        del self.request.session['oauth_verifier']
        self._refresh_followers()
        followers_followers_data = \
            twitter.data.get_processed_followers_followers_data(
                self.api.me().screen_name)
        return Response(followers_followers_data)

    def _refresh_followers(self):
        for follower in limit_handled(
                tweepy.Cursor(self.api.followers).items()
        ):
            self._save_user_follower_relation(self.api.me(), follower)
            self._find_his_followers(follower)

    def _find_his_followers(self, follower):
        for follower_follower in limit_handled(
                tweepy.Cursor(
                    self.api.followers, screen_name=follower.screen_name
                ).items()
        ):
            self._save_user_follower_relation(follower, follower_follower)

    def _save_user_follower_relation(self, this_user, follower):
        """
        It saves in DB relation between logged in twitter user and the follower
        :param this_user: twitter api User
        :param follower: twitter api User
        """
        twitter_user = TwitterUser.object.get_or_create(
            screen_name=this_user.screen_name)
        follower = TwitterUser.objects.get_or_create(
            screen_name=follower.screen_name)
        Follower.objects.get_or_create(
            twitter_user=twitter_user, follower=follower)
