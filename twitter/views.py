
import time

import tweepy

from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from twitter import data
from twitter.auth import (
    redirect_to_twitter_auth,
    get_twitter_api,
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
            print("We have to wait 16 minutes...")
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
        data.remove_old_followers(self.api.me().screen_name)
        self._refresh_followers()
        followers_followers_data = \
            data.get_processed_followers_followers_data(
                self.api.me().screen_name)
        return Response(
            dict(result=followers_followers_data)
        )

    def _refresh_followers(self):
        for follower in limit_handled(
                tweepy.Cursor(self.api.followers).items()
        ):
            data.save_user_follower_relation(
                self.api.me().screen_name, follower.screen_name)
            self._find_his_followers(follower)

    def _find_his_followers(self, follower):
        for follower_follower in limit_handled(
                tweepy.Cursor(
                    self.api.followers, screen_name=follower.screen_name
                ).items()
        ):
            data.save_user_follower_relation(
                follower.screen_name, follower_follower.screen_name)
