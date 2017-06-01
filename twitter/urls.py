
from django.conf.urls import url

from . import views


urlpatterns = (
    url(r'^testlogin/$', views.test_login, name='test-login'),
    url(r'^followers/followers/$', views.followers, name='followers'),
)
