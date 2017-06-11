
import os
import configparser


# Set the consumer key and secret
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'config.ini'))
CONSUMER_KEY = config['oauth']['consumer-key']
CONSUMER_SECRET = config['oauth']['consumer-secret']
CALLBACK_URL = config['oauth']['callback-url']
