
import requests
import urllib3
import hashlib
import random
import time

from .config import CONSUMER_KEY


def followers(token):
    address = (
        'https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name='
        'mlx72&skip_status=true&include_user_entities=false'
    )
    response = requests.get(address)
    return response


# def test(access_token):
#     screen_name = 'programmableweb'
#     url = 'https://api.twitter.com/1.1/statuses/update.json'
#     status = "Hello World @%s!" % screen_name
#     manager = urllib3.PoolManager()
#
#     # Set the parameters required to build the base of the signature, using a dictionary for convenience
#     parameters = {
#         "oauth_consumer_key": CONSUMER_KEY,
#         "oauth_nonce": hashlib.sha1(str(random.random)).hexdigest(),
#         "oauth_signature_method": "HMAC-SHA1",
#         "oauth_timestamp": str(int(time.time())),
#         "oauth_token": access_token['oauth_token'],
#         "oauth_version": "1.0",
#         "status": status
#     }
#
#     # Build the string that forms the base of the signature, iterating through the dictionary and using the key/values in the string
#     base_string = "%s&%s&%s" % (method, urllib.quote(url, ""), urllib.quote(
#         '&'.join(sorted("%s=%s" % (key, value)
#                         for key, value in parameters.iteritems())), ""))
#
#     # Create the signature using signing key composed of consumer secret and token secret obtained during 3-legged dance
#     signature = hmac.hmac.new("%s&%s" % (urllib.quote(CONSUMER_SECRET, ""),
#                                          urllib.quote(access_token[
#                                                           'oauth_token_secret'],
#                                                       "")),
#                               base_string, hashlib.sha1)
#
#     # Add result to parameters and create a string in required format for header
#     parameters['oauth_signature'] = signature.digest().encode("base64").rstrip(
#         '\n')
#     auth_header = 'OAuth %s' % ', '.join(
#         sorted('%s="%s"' % (urllib.quote(key, ""), urllib.quote(value, ""))
#                for key, value in parameters.iteritems() if key != 'status'))
#
#     # Set HTTP headers
#     http_headers = {"Authorization": auth_header,
#                     'Content-Type': 'application/x-www-form-urlencoded'}
#
#     # Send the request
#     response = manager.urlopen("POST", url, headers=http_headers, body=status)
#
#     # Set messages that will be used in modal dialogs
#     if response.status == 200:
#         flask.flash("Tweet sent mentioning @%s" % screen_name)
#     else:
#         flask.flash("Error sending tweet: %s" % response.data)



if __name__ == '__main__':
    r = followers()
    print(r)
