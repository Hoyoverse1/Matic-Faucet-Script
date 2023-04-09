import tweepy
consumer_key = 'masukkan consumer key Anda'
consumer_secret = 'masukkan consumer secret Anda'
access_token = 'masukkan access token Anda'
access_token_secret = 'masukkan access token secret Anda'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def send_tweet(message):
    api.update_status(message)

def reply_to_mentions():
    
    mentions = api.mentions_timeline(since_id=last_mention_id)

    for mention in mentions:
        mention_id = mention.id_str
        mention_text = mention.text
        sender_username = mention.user.screen_name
        reply_text = f'@{sender_username} Terima kasih telah mencantumkan saya!'
        api.update_status(reply_text, in_reply_to_status_id=mention_id)

        last_mention_id = mention_id

reply_to_mentions()
