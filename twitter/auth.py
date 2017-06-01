
# Import required packages, including the oauthlib package discussed earlier in the tutorial
import oauth2
from urllib.parse import parse_qsl

from django.shortcuts import redirect


def request_token():
    # Set the consumer key and secret
    CONSUMER_KEY = "***"
    CONSUMER_SECRET = "***"

    # Create a oauth2.Consumer object that wraps the parameters for the calls to the HTTP endpoints
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)

    # Use the oauth2.Client class to call the Twitter OAuth endpoint
    resp, content = oauth2.Client(consumer).request('https://api.twitter.com/oauth/request_token', "GET")

    # Create a standard dictionary from the response body, using parse_qsl as a convenience to parse the query string in the response
    return dict(parse_qsl(content))


def redirect_to_twitter_login_page(token_data_dir):
    # Redirect user to authorization page, encapsulating request token in URL
    return redirect(
        "%s?oauth_token=%s" % (
            'https://api.twitter.com/oauth/authorize',
            token_data_dir[b'oauth_token'].decode('utf-8')
        )
    )
