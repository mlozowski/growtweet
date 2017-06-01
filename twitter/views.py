
from django.http import HttpResponse

from . import auth


def test_login(request):
    token_data = auth.request_token()
    return auth.redirect_to_twitter_login_page(token_data)


def followers(request):
    return HttpResponse('Jest')
