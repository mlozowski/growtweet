
from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^twitterlogin/$', views.twitter_login, name='twitter-login'),
    url(r'^followers/followers/$', views.followers, name='followers'),
)
