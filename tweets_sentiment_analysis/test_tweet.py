import sentiment_mod as s
import tweet_preprocessor as prep

print(s.sentiment(prep.processTweet("I haaaaate all minions!! I better kill time watching www.youtube.com")))
print(s.sentiment(prep.processTweet("I love minions")))
