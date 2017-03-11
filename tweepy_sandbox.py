import tweepy

auth = tweepy.OAuthHandler('y4466mn59R0Fk0aOgqKPpXHzK', 'BFXyDey7YiG08W5k6sMenk1Lqc7KKwRY3VJl3lCBLDKc36kk7y')
auth.set_access_token('58867345-wukkRMORY7aJvBb795hJmTGxv6rApJFeUibbBDpLp', 'hNsEQkTSQ3qGHv8gizDaAMCxrR0xo1h0gMFojwbf8fUI0')

api = tweepy.API(auth)










#gets userinfo for specified user and writes to file. working
#user_info = api.get_user('agentcooper0115')
#f = open('userdata', 'w')
#s = str(user_info)
#print(s)
#f.write(s)

#updates logged in usere's status. working
#api.update_status('testing harassmentbot again')


#Returns the 20 most recent statuses posted from the authenticating user or the user specified. working
#timeline = api.user_timeline(id="agentcooper0115")
#print(timeline)

#prints public tweets for current user. Working
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print (tweet.text)


#gets id for most rtecent tweet of user. working
#mostrecenttweet = api.user_timeline('agentcooper0115')[0]
#print(mostrecenttweet)
