
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

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
