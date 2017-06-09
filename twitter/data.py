
from twitter.models import (
    Follower,
    TwitterUser,
)


def get_processed_followers_followers_data(screen_name):
    out_data_list = []
    my_followers = Follower.objects.filter(
        twitter_user__screen_name=screen_name)
    followers_followers_all = Follower.objects.filter(
        twitter_user__in=my_followers.values_list('follower', flat=True)
    ).values_list('follower__screen_name', flat=True)
    followers_followers_all = list(followers_followers_all)
    followers_followers_distinct = set(followers_followers_all)
    for follower_follower in followers_followers_distinct:
        out_data_list.append(
            {
                'follower_follower_name': follower_follower,
                'followers_count': followers_followers_all.count(
                    follower_follower)
            }
        )
    return out_data_list


def remove_old_followers(screen_name):
    my_followers = Follower.objects.filter(
        twitter_user__screen_name=screen_name)
    for follower in my_followers:
        follower.follower.delete()
    TwitterUser.objects.filter(screen_name=screen_name).delete()


def save_user_follower_relation(user_name, follower_name):
    """
    It saves in DB relation between logged in twitter user and the follower
    :param user_name: str
    :param follower_name: str
    """
    twitter_user = TwitterUser.object.get_or_create(
        screen_name=user_name)
    follower = TwitterUser.objects.get_or_create(
        screen_name=follower_name)
    Follower.objects.get_or_create(
        twitter_user=twitter_user, follower=follower)
