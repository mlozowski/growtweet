
import tweepy

from django.shortcuts import redirect

from twitter.config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    CALLBACK_URL,
)


def get_twitter_api(request, verifier):
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    token = request.session['request_token']
    del request.session['request_token']
    oauth.request_token = token
    oauth.get_access_token(verifier)
    return tweepy.API(oauth)


def redirect_to_twitter_auth(request):
    oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL)
    redirect_url = oauth.get_authorization_url()
    request.session['request_token'] = oauth.request_token
    return redirect(redirect_url)
