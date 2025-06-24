import instaloader
import time
import sys
# import os
# from dotenv import load_dotenv
# load_dotenv("../.env")

# start_time = time.monotonic()
L = instaloader.Instaloader()

def get_instagram_account_info(username):
    profile = instaloader.Profile.from_username(L.context, username)
    follower_count = profile.followers
    return {'user': username, 'followers': follower_count}

for profile in profiles:
    info = get_instagram_account_info(account)
    account_with_data.append(info)


# time_elapsed = time.monotonic() - start_time

L.close()