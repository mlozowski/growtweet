
import logging
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


def limit_handled(cursor, do_not_wait_after_limit=False):
    """
    It handles Twitter data limitation. We have to wait for 15 minutes
    to another data delivery.
    :param cursor: tweepy.Cursor
    :param do_not_wait_after_limit: boolean
    :return: Next data from response
    """
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            # it is very naive approach, but for such a limited time
            # it has to be enough
            if do_not_wait_after_limit is False:
                logging.info("We have to wait 16 minutes...")
                time.sleep(16 * 60)
            else:
                # Or we can just skip the rest of data and we have
                # Proof of Concept
                logging.warning(
                    "We reached the rate limit and "
                    "we do not wait for the rest of data"
                )
                break


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
        my_name = self.api.me().screen_name
        logging.info(
            "Data for user '{}' is going to be refreshed.".format(my_name)
        )
        del self.request.session['oauth_verifier']
        logging.info("Removing old data...")
        data.remove_old_followers(my_name)
        self._refresh_followers()
        logging.info("Data refreshment completed!")
        followers_followers_data = \
            data.get_processed_followers_followers_data(my_name)
        return Response(
            dict(result=followers_followers_data)
        )

    def _refresh_followers(self):
        logging.info("Starting data refreshment.")
        for follower in limit_handled(
                tweepy.Cursor(self.api.followers).items(),
                do_not_wait_after_limit=True
        ):
            data.save_user_follower_relation(
                self.api.me().screen_name, follower.screen_name)
            self._find_his_followers(follower)

    def _find_his_followers(self, follower):
        for follower_follower in limit_handled(
                tweepy.Cursor(
                    self.api.followers, screen_name=follower.screen_name
                ).items(),
                do_not_wait_after_limit=True
        ):
            data.save_user_follower_relation(
                follower.screen_name, follower_follower.screen_name)


class CurrentFollowers(APIView):
    def get(self, request, user_name):
        return Response(
            dict(result=data.get_processed_followers_followers_data(user_name))
        )
