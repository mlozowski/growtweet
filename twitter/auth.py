
import oauth2
from urllib.parse import parse_qsl

from django.shortcuts import redirect

from .config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    TOKEN_SECRET,
    REQUEST_TOKEN_ADDRESS,
    TWITTER_LOGIN_ADDRESS,
    TWITTER_ACCESS_TOKEN_ADDRESS,
)


def request_token():
    # Create a oauth2.Consumer object that wraps the parameters
    # for the calls to the HTTP endpoints
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

    # Use the oauth2.Client class to call the Twitter OAuth endpoint
    resp, content = oauth2.Client(consumer).request(
        REQUEST_TOKEN_ADDRESS, "GET")

    # Create a standard dictionary from the response body, using parse_qsl as
    # a convenience to parse the query string in the response
    return dict(parse_qsl(content))


def redirect_to_twitter_login_page(token_data_dir):
    """
    Redirect user to authorization page, encapsulating request token in URL
    :param token_data_dir: dir
    :return: redirect
    """
    return redirect(
        "%s?oauth_token=%s" % (
            TWITTER_LOGIN_ADDRESS,
            token_data_dir[b'oauth_token'].decode('utf-8')
        )
    )


def access_data(oauth_token, oauth_verifier):
    """
    Get access token and other related data in form
    {"user_id": "2343", "x_auth_expires": "0", "screen_name": "jjsdh", "
    oauth_token": "HFYFTUT", "oauth_token_secret": "RDYTTYFYTGF"}
    :param oauth_token: str
    :param oauth_verifier: str
    :return: dict
    """
    token = oauth2.Token(oauth_token, TOKEN_SECRET)
    token.set_verifier(oauth_verifier)
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(
        TWITTER_ACCESS_TOKEN_ADDRESS, "POST")
    access_token = dict(parse_qsl(content.decode('utf-8')))
    return access_token, resp
