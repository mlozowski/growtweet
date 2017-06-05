
import oauth2
from urllib.parse import parse_qsl

from django.shortcuts import redirect

from .config import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    REQUEST_TOKEN_ADDRESS,
    TWITTER_LOGIN_ADDRESS,
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
    # Redirect user to authorization page, encapsulating request token in URL
    return redirect(
        "%s?oauth_token=%s" % (
            TWITTER_LOGIN_ADDRESS,
            token_data_dir[b'oauth_token'].decode('utf-8')
        )
    )
