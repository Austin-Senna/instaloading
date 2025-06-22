from selenium import webdriver

accounts = ["austin.senna", "keisharch", "max3bld", "bimaarexa", "ishawngabriel", "maulanasatyaad",
            "dean.hartono"]
account_with_data = []
driver = webdriver.Chrome()

def get_instagram_account_info(username):
    driver.get(f"https://www.instagram.com/{username}/")
    timer = 0
    while True:
        try:
            follower_parent = driver.find_element("xpath", "//span[contains(text(), ' followers')]")
            follower_count_text = follower_parent.find_element("xpath", ".//span").text
            break
        except:
            driver.implicitly_wait(0.25)
            timer += 0.25
            if timer > 5:
                follower_count_text = 'N/A'
                break
    return {'user': username, 'followers':follower_count_text, 'likes': 'N/A'}

for account in accounts:
    info = get_instagram_account_info(account)
    account_with_data.append(info)

print(account_with_data)

driver.quit()

