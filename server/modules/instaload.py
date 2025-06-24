import instaloader

class Instaloader: 
    def __init__(self, driver):
        self.driver = driver    
        self.instagramList = []

    def get_instagram_account_info(self, username):
        L = self.driver
        profile = instaloader.Profile.from_username(L.context, username)
        follower_count = profile.followers
        picture = profile.profile_pic_url
        self.instagramList.append({"IG_User": username, "IG_Followers": follower_count, 
                                   "PicURL" : picture})

    def get_instagram_list(self):
        return self.instagramList
