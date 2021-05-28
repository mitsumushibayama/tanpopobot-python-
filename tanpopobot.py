import time
import tweepy
import config
import text

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

API = tweepy.API(auth)

followers_id_list = API.followers_ids()

if followers_id_list != []:
    for follower in followers_id_list:
        API.create_friendship(follower)
else:
    print("none followers")

status = API.mentions_timeline()

for mention in status:
    print(mention.user)

    if mention.retweeted:
        continue

    if mention.user.following == False:
        continue

    mentiontime = mention.created_at.timestamp()
    nowtime = time.time()

    if nowtime - mentiontime < 32700:
        word = text.chooseword()
        reply_text = "@"+str(mention.user.screen_name)+" "+word
        API.update_status(status = reply_text, in_reply_to_status_id = mention.id)

#time.sleep(300)

