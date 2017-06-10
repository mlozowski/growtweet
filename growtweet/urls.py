
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

from growtweet import views


schema_view = get_swagger_view(title='GrowTweet API')


urlpatterns = [
    url(r'^$', views.Main.as_view(), name='main-page'),
    url(r'^', include('twitter.urls')),
    url(r'^api/$', schema_view, name='api-docs'),
]
