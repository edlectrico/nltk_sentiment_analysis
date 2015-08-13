## Sentiment Analysis from Twitter
This repo provides the needed tools to perform sentiment analysis to data collected from Twitter. In this first version the data is appended to the test_tweet.py script as a string.

###Contents
* data/: Two files with positive and negative opinions from different movies to train the classifiers.
* tweet_preprocessor.py: Several functions to preprocess tweet content. For example, removing URLs, usernames, etc.
* sentiment_train.py: It creates, configures and trains different classification algorithms to finally generate a classifier from the results of the others (as a voting strategy). Notice that the classifiers are saved to a 'pickled_algos' folder, so I highly recommend that you create that folder (I do not provide the algorithm files as they are automatically generated when running this script).
* sentiment_mod.py: It loads all algorithms (from the 'pickled_algos' folder) and defines a global input method to make the classification of the desired text:
```
def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)
```
* test_tweet.py: The launcher. You can add here your text to be analysed.
```
import sentiment_mod as s

print(s.sentiment("I hate all minions"))
print(s.sentiment("I love minions"))
```
###The Output
If everything is fine, it should give you an output with the classification for the tweet as 'pos' or 'neg' and the level of confidence for each classification:
```
('neg', 1.0)
('pos', 1.0)
```