
from django.conf.urls import url


from . import views


urlpatterns = (
    url(r'^twitterlogin/$', views.twitter_login, name='twitter-login'),
    url(r'^followers/followers/$',
        views.Followers.as_view(), name='followers'),
    url(r'^getfollowers/?$',
        views.GetRefreshedFollowers.as_view(), name='get-followers'),
    url(r'^currentfollowers/(?P<user_name>[\w-]+)/?$',
        views.CurrentFollowers.as_view(), name='current-followers'),
)
