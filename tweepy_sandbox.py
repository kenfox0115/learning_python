import tweepy

auth = tweepy.OAuthHandler('y4466mn59R0Fk0aOgqKPpXHzK', 'BFXyDey7YiG08W5k6sMenk1Lqc7KKwRY3VJl3lCBLDKc36kk7y')
auth.set_access_token('58867345-wukkRMORY7aJvBb795hJmTGxv6rApJFeUibbBDpLp', 'hNsEQkTSQ3qGHv8gizDaAMCxrR0xo1h0gMFojwbf8fUI0')

api = tweepy.API(auth)

API.user_timeline(  )





























#prints public tweets for current user
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print (tweet.text)