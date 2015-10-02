import re

def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def processTweet(tweet):
    tweet = replaceTwoOrMore(tweet)
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet)
    tweet = re.sub('@[^\s]+',' ',tweet)
    tweet = re.sub('[\s]+',' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    # tweet = re.sub(',',"", tweet)
    tweet = re.sub(r'[!|?|¿|¡]','', tweet)
    tweet = re.sub('(rt)',r'', tweet)
    tweet = re.sub(r'[?|$|.|!]',r'', tweet)
    tweet = tweet.strip('\'"')
    #print (tweet)
    return tweet

