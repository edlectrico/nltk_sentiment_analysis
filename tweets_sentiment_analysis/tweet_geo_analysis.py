import sentiment_mod as s
import tweet_preprocessor as prep
import language_detector as lang

class TweetGeo:
	def __init__(self, id, created_at, text, time_zone, latitude, longitude, country_code):
		self.id = id
		self.text = text
		self.created_at = created_at
		self.time_zone = time_zone
		self.latitude = latitude
		self.longitude = longitude
		self.country_code = country_code

tweets = open('data/tweets_1000_geo_clean.csv', 'r')
# We are going to create a new .csv file which will contain
# the classification of the tweet (pos|neg), the date and
# the location
classified_tweets = open('output/classified_1000_tweets.csv', 'a')

# l = 'created_at, text, time_zone, latitude, longitude, contry_code'
#cont = 0
for l in tweets:
#	if cont != 0:
		country_code = l.rsplit(',', 6)[6]
		longitude = l.rsplit(',', 6)[5]
		latitude = l.rsplit(',', 6)[4]
		time_zone = l.rsplit(',', 6)[3] 
		text = l.rsplit(',', 6)[2]  
		created_at = l.rsplit(',', 6)[1]
		id = l.rsplit(',', 6)[0]		

		text = prep.processTweet(text) # Deleting URLs, usernames, etc
		tg=TweetGeo(id, created_at, text, time_zone, latitude, longitude, country_code)
		tweet_lang = lang.detect_language(tg.text)
		tweet_classification = s.sentiment(tg.text)[0]
		classified_tweets.write(tweet_classification + ',' + tg.id + ',' + tg.created_at + ',' + tweet_lang + ',' + tg.text + ',' + tg.time_zone + ',' + tg.latitude + ',' + tg.longitude + ',' + tg.country_code)
#		cont+=1
#	else:
#		cont += 1
#		break

tweets.close()
classified_tweets.close()
