
from django.http import HttpResponse
from django.views.generic import View

from .auth import (
    redirect_to_twitter_auth,
    get_twitter_api,
)


def twitter_login(request):
    return redirect_to_twitter_auth(request)


class Followers(View):
    def get(self, request):
        api = get_twitter_api(request)
        followers_data = api.followers()
        return HttpResponse('jest')
