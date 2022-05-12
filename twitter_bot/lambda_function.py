import tweepy
import json
import random

data = json.load(open('total_lyrics.json'))

# filter out anything we dont want
new_data = []
for line in data:

    if line.strip() != '':
        # if it is not empty add it to the new list of lines of lyrics
        new_data.append(line)


def lambda_handler(event, context):
    client = tweepy.Client(bearer_token="xxx",
                    access_token='xxx',
                    access_token_secret='xxx',
                    consumer_key='xxx',
                    consumer_secret='xxx')

    random_tweet = random.choice(new_data) + '\n' + random.choice(new_data) + '\n' + random.choice(new_data) + '\n' + random.choice(new_data) + '\n' + random.choice(new_data) + '\n' 

    # now random_tweet is 5 lines from all the lines

    print(random_tweet)
    response = client.create_tweet(
        text = random_tweet
    )

