## Setup ##
# Variables
screenName = '@wbz'
numberTweets = 10

# twitter keys
rapidapi_key =

api_key =
api_key_secret = 
access_token = 
access_token_secret = 

# google keys
bearer_token = 
g_api_key = 
g_url = 'https://language.googleapis.com/v1beta2/documents:analyzeSentiment?key='

## Botometer ##
!pip install botometer
import botometer

twitter_app_auth = {
    'consumer_key': api_key,
    'consumer_secret': api_key_secret,
    'access_token': access_token,
    'access_token_secret': access_token_secret,
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account(screenName)

main_language = result['user']['majority_lang']
prob_bot = result['cap']['english']
overall_score = result['display_scores']['english']['overall']
fake_follower_score = result['display_scores']['english']['fake_follower']
self_declared_bots_score = result['display_scores']['english']['self_declared']
manually_labeled_bot_score = result['display_scores']['english']['astroturf']
spammer_bot_score = result['display_scores']['english']['spammer']
financial_bot_score = result['display_scores']['english']['financial']
other_bot_score = result['display_scores']['english']['other']

print("ACCOUNT BOT SCORE")
print("__________________________________")
print("Screen Name:             ",screenName)
print("Main Language:           ", main_language)
print("Bot Probability:         ", round(100*prob_bot,ndigits=2),"%")
print("Overall Score:           ", overall_score)
print("   Fake Follower:        ", fake_follower_score)
print("   Self Declared Bot:    ", self_declared_bots_score)
print("   Manually Labelled Bot:", manually_labeled_bot_score)
print("   Spammer Bot:          ", spammer_bot_score)
print("   Financial Bot:        ", financial_bot_score)
print("   Other Bot:            ", other_bot_score)

## Pull tweets
!pip install tweepy

import tweepy
# authentication of API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# make API instance
api = tweepy.API(auth)

# get the user's tweets
tweets = api.user_timeline(screen_name=screenName, count=numberTweets, tweet_mode='extended')

i=1
print(screenName + '`s last ', numberTweets, 'tweets:\n')
for tweet in tweets:
  print(i,tweet.full_text)
  print(' (', tweet.retweet_count, 'retweets | tweeted at', tweet.created_at, ')\n')
  i=i+1

## Google NLP ##
import requests
import json

headers = {
    'Authorization': bearer_token,
    'Accept': 'application/json',
}

magnitudes = []
scores = []
retweets = []

# collect sentiment data for each tweet
for tweet in tweets:
  json_data = {
      'document': {
          'content': tweet.full_text,
          'type': 'PLAIN_TEXT',
      },
  }

  response = requests.post(g_url + g_api_key, headers=headers, json=json_data)
  sentiment = json.loads(response.text)

  magnitudes.append(sentiment['documentSentiment']['magnitude'])
  scores.append(sentiment['documentSentiment']['score'])
  retweets.append(tweet.retweet_count)

import numpy as np

scores = np.array(scores)
magnitudes = np.array(magnitudes)
retweets = np.array(retweets)

avg_score = np.mean(scores)
avg_magnitude = np.mean(magnitudes)
avg_retweets = np.mean(retweets)
weighted_score = round(np.sum(scores*magnitudes)/np.sum(magnitudes), 2)

print('AVERAGE SENTIMENT:              ', avg_score)
print('AVERAGE SENTIMENT MAGNITUDE:    ',avg_magnitude)
print('AVERAGE RETWEETS:               ', avg_retweets)
print('WEIGHTED SENTIMENT BY MAGNITUDE:', weighted_score)

print('\nINDIVIDUAL SENTIMENTS:', scores)
print('INDIVIDUAL MAGNITUDES:', magnitudes)
print('INDIVIDUAL RETWEETS:  ', retweets)

## Overall Impressions of user ##

# bot probability
if (prob_bot>0.9):
  bot = 'DEFINITELY A BOT'
elif(prob_bot>0.7):
  bot = 'MAYBE A BOT'
elif(prob_bot>0.5):
  botometer = 'LIKELY NOT A BOT'
else:
  bot = 'NOT A BOT'

# positivity
if (weighted_score>0.5):
  sent = 'VERY POSITIVE'
elif(weighted_score>0):
  sent = 'POSITIVE'
elif(weighted_score>-0.5):
  sent = 'NEGATIVE'
else:
  sent = 'VERY NEGATIVE'

# emotionality
if (avg_magnitude>10):
  expr = 'EMOTIONAL TONE'
else:
  expr = 'NEUTRAL TONE'

# influence
if (avg_retweets>20):
  infl = 'INFLUENTIAL'
else:
  infl = 'NOT INFLUENTIAL'

print('User', screenName, 'is a', bot, ', uses', sent, 'language and', expr, ', and is', infl)
