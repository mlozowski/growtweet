
from django.views.generic import View
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .auth import (
    redirect_to_twitter_auth,
    get_twitter_api,
)


def twitter_login(request):
    return redirect_to_twitter_auth(request)


class Followers(View):
    template_name = 'twitter/followers.html'

    def get(self, request):
        verifier = request.GET.get('oauth_verifier', None)
        if verifier is not None:
            request.session['oauth_verifier'] = verifier
            return render(request, self.template_name, {'loading': True})
        else:
            return render(request, self.template_name, {'loading': False})


class GetFollowers(APIView):
    def get(self, request):
        if request.GET.get('refresh', 'no') == 'yes':
            data = self._refresh_followers()
        else:
            data = self._last_data()
        return Response(data)

    def _refresh_followers(self):
        verifier = self.request.session['oauth_verifier']
        api = get_twitter_api(self.request, verifier)
        del self.request.session['oauth_verifier']
        followers = api.followers()
        return {'refreshed': True}

    def _last_data(self):
        return {'refreshed': False}
