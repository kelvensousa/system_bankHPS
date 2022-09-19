import tweepy

consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "
auth = tweepy.OAuthHandleruthHandler()
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
screen_name = "geeksforgeeks"
user = api.get_user(screen_name)
ID = user.id_str

print("The ID of the user is : " + ID)
