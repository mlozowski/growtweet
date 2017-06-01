
from django.conf.urls import url, include

from growtweet import views

urlpatterns = [
    url(r'^$', views.Main.as_view(), name='main-page'),
    url(r'^', include('twitter.urls')),
]
