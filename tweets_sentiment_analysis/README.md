## Sentiment Analysis from Twitter Data
This repo provides the needed tools to perform sentiment analysis to data collected from Twitter.

###Contents
* **data/**: It contains:
 - two files with positive and negative opinions from different movies to train the classifiers. 
 - the geo_tweets.csv for the tweet_geo_analysis.py script and the cities_formatted.csv with formatted information about cities with more than 1000 people, including name, latitude and longitude, country code, etc.
 - the all_words.txt file, which includes a tuple of tweet_id and word for each tweet text written in english.
* **cities_geonames.py**: A small script which reads each line from data/cities1000.txt and generates a formatted output of cities and their most relevant information to output/formatted_cities.csv.
* **language_detector.py**: A simple tool to determine the language of the text. Usage:
```
> python3 language_detector.py 'Hi, this is a language test'
english
```
* **tweet_geo_analysis.py**: This script offers a method to analyse a .csv file of tweets (in this case 'data/tweets_1000_geo_clean.csv') generated with Hive. It reads each line (geo_tweet) and parses the text determining if is positive or negative. Finally, it stores each geo_tweet as a new line containing the sentiment classification, creation date and location (see the output file 'output/classified_1000_tweets.csv').
```
We have thousands of tweets loaded in HDFS. With Hive we create a tweets table which contains every field of the tweet structure. 
Then, we create a geo_tweets table which contains only the text, creation date and location of each tweet of the tweets table. 
Through HUE we download the resulting geo_tweets table as a .csv, which is the one in the data folder used as input.
```
* **tweet_preprocessor.py**: Several functions to preprocess tweet content. For example, removing URLs, usernames, etc.
* **sentiment_train.py**: It creates, configures and trains different classification algorithms to finally generate a classifier from the results of the others (as a voting strategy). Notice that the classifiers are saved to a 'pickled_algos' folder, so I highly recommend that you create that folder (I do not provide the algorithm files as they are automatically generated when running this script).
* **sentiment_mod.py**: It loads all algorithms (from the 'pickled_algos' folder) and defines a global input method to make the classification of the desired text:
```
def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
```
* **test_tweet.py**: The launcher. You can add here your text to be analysed.
```
import sentiment_mod as s

print(s.sentiment("I hate all minions"))
print(s.sentiment("I love minions"))
```
###The Output
* **test_tweet.py**: It contains sample text strings. If everything is fine, it should give you an output with the classification for the tweet as 'pos' or 'neg' and the level of confidence for each classification:
```
> python3 test_tweet.py
('neg', 1.0)
('pos', 1.0)
```
* **tweet_geo_analysis.py**: It reads from 'data/tweets_1000_geo_clean.csv' and generates a new output file ('output/classified_1000_tweets.csv') with the following fields:
  - The tweet sentiment classification (pos or neg)
  - The tweet id
  - The creation date
  - The language of the tweet (not 100% accurate)
  - The text of the tweet
  - The city from where it has been tweeted
  - The coordinates
  - The country code or time zone
  ```
> python3 tweet_geo_analysis.py
10664
```
