from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
start_time = time.monotonic()

accounts = ["joshuamsolomon_", "giselagwenm", "rosyelins", "kendrickliusbong", "daniel_markk_", 
            "mauladzima", "ishawngabriel", "vanneswij2", "irrachional", "hitapryhita", 
            "arkanfadhil_"]
account_with_data = []


chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

def get_tiktok_account_info(username):
    driver.get(f"https://www.tiktok.com/@{username}")

    timer = 0
    driver.implicitly_wait(0.5)
    
    while True:
        try:
            follower_count = driver.find_element("xpath", "//strong[@title='Followers']")
            follower_count_text = follower_count.text
            like_count = driver.find_element("xpath", "//strong[@title='Likes']")
            like_count_text = like_count.text
            break
        except:
            driver.implicitly_wait(0.25)
            timer += 0.25
            if timer > 5:
                follower_count_text = 'N/A'
                like_count_text = 'N/A'
                break

    return {'user': username, 'followers':follower_count_text, 'likes': like_count_text}

for account in accounts:
    info = get_tiktok_account_info(account)
    account_with_data.append(info)

print(account_with_data)
print(time.monotonic() - start_time, "seconds")

driver.quit()


# Try this with playwright, but it doesnt work for me :(
# from TikTokApi import TikTokApi
# import asyncio

# api = TikTokApi()
# accounts = [
#         "joshuamsolomon_", "giselagwenm", "rosyelins", "kendrickliusbong", "daniel_markk_",
#         "mauladzima", "ishawngabriel", "vanneswij2", "irrachional", "hitapryhita",
#         "arkanfadhil_"
# ]

# account_with_data = []

# async def search_user(username):
#     await api.create_sessions()
#     user = api.user(username)
#     info = await user.info()
#     print(info)

# asyncio.run(search_user("arkanfadhil_"))



