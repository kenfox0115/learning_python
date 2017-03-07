import tweepy
import time
from random import randint

auth = tweepy.OAuthHandler('y4466mn59R0Fk0aOgqKPpXHzK', 'BFXyDey7YiG08W5k6sMenk1Lqc7KKwRY3VJl3lCBLDKc36kk7y')
auth.set_access_token('58867345-wukkRMORY7aJvBb795hJmTGxv6rApJFeUibbBDpLp', 'hNsEQkTSQ3qGHv8gizDaAMCxrR0xo1h0gMFojwbf8fUI0')

api = tweepy.API(auth)

# initially, the script will assume that the last tweet was a null value
lasttweet = api.user_timeline('jonnytestsalot')[0]

# What the bot will tweet
#filename = open('twain.txt', 'r')
tweettext = '@jonnytestsalot I continue to heckle you'
#filename.close()



# this is the function that does most of the work of the bot
def runTime():

    # uses the global lasttweet variable, rather than the local one
    global lasttweet

    # gets the most recent tweet by @ocertat and prints its id
    mostrecenttweet = api.user_timeline('jonnytestsalot')[0]
    print(mostrecenttweet.id)

    # compares the two tweets, and tweets a line of Twain
    # if there is a new tweet from @ocertat
    if mostrecenttweet != lasttweet:
        line = tweettext
        api.update_status(status=line,in_reply_to_status_id=mostrecenttweet.id)
        print(line)

    # updates lasttweet to the most recent tweet
    lasttweet = mostrecenttweet

# runs the main function every 5 seconds
while True:
    runTime()
    print("sleeping")
    time.sleep(5)  # Sleep for 5 seconds

