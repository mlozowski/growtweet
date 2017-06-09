
from twitter.models import Follower


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
