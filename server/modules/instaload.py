import instaloader
import time
import sys
# import os
# from dotenv import load_dotenv
# load_dotenv("../.env")

start_time = time.monotonic()
L = instaloader.Instaloader()

accounts = ["austin.senna", "keisharch", "max3bld", "bimaarexa", "ishawngabriel", "maulanasatyaad",
            "dean.hartono"]
account_with_data = []

def get_instagram_account_info(username):
    profile = instaloader.Profile.from_username(L.context, username)
    follower_count = profile.followers
    return {'user': username, 'followers': follower_count}

for account in accounts:
    info = get_instagram_account_info(account)
    account_with_data.append(info)


time_elapsed = time.monotonic() - start_time
print(account_with_data)
sys.stdout.flush()

L.close()