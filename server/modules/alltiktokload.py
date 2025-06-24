from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sys
import json
import tiktokload

# start_time = time.monotonic()
profiles = json.load(open('./db/initialDB.json'))

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-webrtc")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=chrome_options)

tiktokloader = tiktokload.TiktokLoader(driver)

for profile in profiles:   
    tiktokloader.get_tiktok_account_info(profile["Name"], profile["Tiktok"])

print(json.dumps(tiktokloader.get_tiktok_list()))
# print(time.monotonic()-start_time)

driver.quit()


# Try this with playwright, but it doesnt work for me :(
# from TikTokApi import TikTokApi
# import asyncio

# api = TikTokApi()

# account_with_data = []

# async def search_user(username):
#     await api.create_sessions()
#     user = api.user(username)
#     info = await user.info()
#     print(info)

# asyncio.run(search_user("arkanfadhil_"))



