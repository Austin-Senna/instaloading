import instaloader
import time
import sys
import json
import instaload
import os
from dotenv import load_dotenv
load_dotenv("../.env")

start_time = time.monotonic()
profiles = json.load(open('../db/initialDB.json'))

L = instaloader.Instaloader()
L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
instaloadObject = instaload.Instaloader(L)


for profile in profiles:
    try:
        instaloadObject.get_instagram_account_info(profile["IG"])
    except Exception as e:
        print(f"Failed for {profile['IG']}: {e}")
    time.sleep(2)
    
print(instaloadObject.get_instagram_list())


time_elapsed = time.monotonic() - start_time

L.close()