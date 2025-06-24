class TiktokLoader:
    def __init__(self, driver):
        self.driver = driver
        self.tiktokList = []

    def get_tiktok_account_info(self, name, username):
        driver = self.driver

        if (username == "-"):
            return {'user': username, 'followers':0, 'likes':0}    
        
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
        
        self.tiktokList.append({'name': name, 'TT_user': username, 
                            'TT_followers':follower_count_text, 'TT_likes': like_count_text})
        
    def get_tiktok_list(self):
        return self.tiktokList
    



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



