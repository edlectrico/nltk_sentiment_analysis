import sentiment_mod as s
import tweet_preprocessor as prep

class TweetGeo:
	def __init__(self, text, created_at, location):
        	self.text = text
        	self.created_at = created_at
        	self.location = location

'''
The geo_tweets.csv has been downloaded from a Hive query, choosing
from thousands of tweets the text, created_at and location fields.
To do so, a new table in Hive is needed, created as follows:
CREATE TABLE geo_tweets AS SELECT text, created_at, location FROM tweets;
When the table is created we download the result .csv from HUE (it allows
to download queries results in several formats) through a
SELECT * FROM geo_tweets;
'''
tweets = open('data/geo_tweets.csv', 'r')
# We are going to create a new .csv file which will contain
# the classification of the tweet (pos|neg), the date and
# the location
classified_tweets = open('output/classified_tweets.csv', 'a')

# l = 'text, created_at, location'
for l in tweets:
	# We split each line by comma from the end of the line (rsplit)
	# and taking 2 commas: l.rsplit(',', 2) -> ['text', ' created_at', ' location']
	location = l.rsplit(',', 2)[2]   # pos[2] = ' location'
	created_at = l.rsplit(',', 2)[1] # pos[1] = ' created_at' 
	text = l.rsplit(',', 2)[0]	 # pos[0] = 'text'
	#text = l.replace(location, "").replace(created_at, "")
	text = prep.processTweet(text) # Deleting URLs, usernames, etc
	tg=TweetGeo(text, created_at, location)
	tweet_classification = s.sentiment(tg.text)[0]
	classified_tweets.write(tweet_classification +', ' + tg.created_at + ', ' + tg.location + '\n')

tweets.close()
classified_tweets.close()
