
import os
import configparser


# Set the consumer key and secret
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))
CONSUMER_KEY = config['oauth']['consumer-key']
CONSUMER_SECRET = config['oauth']['consumer-secret']
REQUEST_TOKEN_ADDRESS = config['oauth']['request-token-address']
TWITTER_LOGIN_ADDRESS = config['oauth']['twitter-login-address']
TWITTER_ACCESS_TOKEN_ADDRESS = config['oauth']['twitter-access-token-address']
