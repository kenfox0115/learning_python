import csv
import random


# choose a line form the statuses csv
replies = dict(csv.reader(open("tweets.csv")))
randreply = random.choice(list(replies.keys()))
tweetthis = replies[randreply]


# choose a line form the adjectives csv
adjectives = dict(csv.reader(open("adjectives.csv")))
randadjective = random.choice(list(adjectives.keys()))
tweetadj = adjectives[randadjective]


# combine tweet and adjective in to a single line
total_tweet = tweetthis + tweetadj

# print total line to be tweeted
print(total_tweet)




