from twython import Twython
twitter = Twython('y4466mn59R0Fk0aOgqKPpXHzK', 'BFXyDey7YiG08W5k6sMenk1Lqc7KKwRY3VJl3lCBLDKc36kk7y','58867345 - wukkRMORY7aJvBb795hJmTGxv6rApJFeUibbBDpLp', 'hNsEQkTSQ3qGHv8gizDaAMCxrR0xo1h0gMFojwbf8fUI0')




#verifycreds = twitter.verify_credentials()
#print(verifycreds)



user_timeline = twitter.get_user_timeline(screen_name='ryanmcgrath')
#user_timeline = twitter.get_home_timeline()
print(user_timeline)


#results = twitter.cursor(twitter.search, q='python')
#for result in results:
#    print result


