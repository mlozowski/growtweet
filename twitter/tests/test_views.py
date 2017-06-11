
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
        self.assertEqual(r.status_code, 302)
