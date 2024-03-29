from persona import Person
import tweepy
from datetime import datetime, date, time, timedelta
from credenciales import consumer_key, consumer_secret, access_token,access_token_secret

people = []

def twitter(screen_name):
    for person in people:
        if person.screen_name == screen_name:
            return person.__dict__

    api = get_api(consumer_key, consumer_secret, access_token, access_token_secret)

    user = None
    try:
        user = api.get_user(screen_name)
    except tweepy.error.TweepError:
        return {"Error":"Username Not Found"}
    tweets_count = user.statuses_count
    account_created_date = user.created_at
    followers_count = user.followers_count
    days = (datetime.utcnow() - account_created_date).days

    timeline = []
    for status in tweepy.Cursor(api.user_timeline, screen_name='@'+screen_name).items():
        timeline.append({"text":status._json["text"],"created_at":status._json["created_at"]})

    avg = float(tweets_count)/float(days)
    person = Person(screen_name,tweets_count,followers_count,days,timeline,avg)
    people.append(person)
    return person.__dict__

def get_api(consumer_key, consumer_secret, access_token, access_token_secret):
    CONSUMER_KEY = consumer_key
    CONSUMER_SECRET = consumer_secret

    ACCESS_TOKEN = access_token
    ACCESS_TOKEN_SECRET = access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
