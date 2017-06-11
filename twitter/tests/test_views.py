
from unittest.mock import (
    patch,
    MagicMock,
)

from django.test import (
    TestCase,
    Client,
)


class TwitterLoginTest(TestCase):
    @patch('tweepy.OAuthHandler')
    def test_twitter_login(self, mocked_oauth_handler):
        magic_mock = MagicMock()
        magic_mock.get_authorization_url.return_value = 'http://some_url/'
        magic_mock.request_token = {'token': 'adsd'}
        mocked_oauth_handler.return_value = magic_mock
        client = Client()
        r = client.get('/twitterlogin/')
        self.assertEquals(r.status_code, 302)


class FollowersTest(TestCase):
    def test_followers_with_oauth_verifier(self):
        client = Client()
        r = client.get('/followers/followers/?oauth_verifier=jgdsfjsdfjfh')
        self.assertTrue(
            'Collecting data in progress.' in r.content.decode('utf-8'))
        self.assertEquals(r.status_code, 200)

    def test_followers_without_oauth_verifier(self):
        client = Client()
        r = client.get('/followers/followers/')
        self.assertTrue(
            'First you have to authenticate with Twitter' in
            r.content.decode('utf-8'))
        self.assertEquals(r.status_code, 200)
