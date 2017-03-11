import csv
import random



replies = dict(csv.reader(open("example.csv")))
randreply = random.choice(list(replies.keys()))
tweetthis = replies[randreply]

print(tweetthis)













#with open('example.csv') as status_list:
#    raw_status = csv.reader(status_list, delimiter=';')
#    for row in raw_status:
#        chosen_to_tweet = random.choice(row)
#        print(chosen_to_tweet)

#for row in csv.reader(open('example.csv'), delimiter=';'):
 #   print(row)