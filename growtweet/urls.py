
from django.conf.urls import url

from growtweet import views

urlpatterns = [
    url(r'^$', views.Main.as_view(), name='main-page'),
]
