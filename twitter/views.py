
import json

from django.http import HttpResponse
from django.views.generic import View

from . import auth
from . import api


def twitter_login(request):
    token_data = auth.request_token()
    return auth.redirect_to_twitter_login_page(token_data)


class Followers(View):
    def get(self, request):
        oauth_token = request.GET.get('oauth_token', None)
        oauth_verifier = request.GET.get('oauth_verifier', None)
        if oauth_token is not None and oauth_verifier is not None:
            access_data, response = auth.access_data(
                oauth_token, oauth_verifier)
            followers_data = api.followers(access_data['oauth_token'])
            return HttpResponse(json.dumps(followers_data))
        else:
            raise NotImplemented
