!pip install botometer

import botometer

screenName = '@wbz'

rapidapi_key = "<Insert> (not storing on github at the moment)"
twitter_app_auth = {
    'consumer_key': '<Insert> (not storing on github at the moment)',
    'consumer_secret': '<Insert> (not storing on github at the moment)',
    'access_token': '<Insert> (not storing on github at the moment)',
    'access_token_secret': '<Insert> (not storing on github at the moment)',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account(screenName)
print(result)

# Store the results
main_language = result['user']['majority_lang']
prob_bot = result['cap']['english']
overall_score = result['display_scores']['english']['overall']
fake_follower_score = result['display_scores']['english']['fake_follower']
self_declared_bots_score = result['display_scores']['english']['self_declared']
manually_labeled_bot_score = result['display_scores']['english']['astroturf']
spammer_bot_score = result['display_scores']['english']['spammer']
financial_bot_score = result['display_scores']['english']['financial']
other_bot_score = result['display_scores']['english']['other']

# Print the results nicely
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
