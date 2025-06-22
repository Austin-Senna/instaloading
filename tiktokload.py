from selenium import webdriver
import requests

accounts = ["joshuamsolomon_", "giselagwenm", "rosyelins", "kendrickliusbong", "daniel_markk_", 
            "mauladzima", "ishawngabriel", "vanneswij2", "irrachional", "hitapryhita", 
            "arkanfadhil_"]
account_with_data = []


driver = webdriver.Chrome()

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

driver.quit()


