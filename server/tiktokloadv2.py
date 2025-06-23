from TikTokApi import TikTokApi
import asyncio

api = TikTokApi()

async def user_example():
    accounts = [
        "joshuamsolomon_", "giselagwenm", "rosyelins", "kendrickliusbong", "daniel_markk_",
        "mauladzima", "ishawngabriel", "vanneswij2", "irrachional", "hitapryhita",
        "arkanfadhil_"
    ]
    account_with_data = []

    for account in accounts:
        try:
            await api.create_sessions()
            user = api.user(username=account)
            info = await user.info()
            followers = info['user']['stats']['followerCount']
            likes = info['user']['stats']['heartCount']
            account_with_data.append({'user': account, 'followers': followers, 'likes': likes})
        except Exception as e:
            print(f"Error fetching data for {account}: {e}")

    print(account_with_data)

asyncio.run(user_example())