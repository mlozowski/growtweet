
from django.db import models


class TwitterUser(models.Model):
    screen_name = models.CharField(max_length=250, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    twitter_user = models.ForeignKey(
        TwitterUser, related_name='follower_twitter_user')
    follower = models.ForeignKey(
        TwitterUser, related_name='follower_follower')
    creation_date = models.DateTimeField(auto_now_add=True)
