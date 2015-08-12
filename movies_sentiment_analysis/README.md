
##Sentiment analysis from NLTK movie_reviews
In this example several classification algorithms are launched. However, considering that each one has its own results (sometimes they are very different), a combination of their performance has been developed as a voting strategy.

##Running the example
Obviously, if you've been through the installation steps you've noticed that Python 3 is required. To run the example you just need to run the following command:
```
$ python3 nltk_movies_classification.py
```
If you don't want to train each classifier each time, there is an example within the code of how to save each classifier to an external pickle file. For the NaiveBayes classifier, for example, you should do:
```
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
```
Then, to load it:
```
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()
```
##Analysing the output
You should expect and output similar to the following one:
```
$ python3 nltk_movies_classification.py 
Most Informative Features
                 winslet = True              pos : neg    =      9.1 : 1.0
                reminder = True              pos : neg    =      9.1 : 1.0
               illogical = True              neg : pos    =      8.9 : 1.0
            wisecracking = True              neg : pos    =      7.6 : 1.0
                    coen = True              pos : neg    =      6.7 : 1.0
                  elmore = True              pos : neg    =      5.7 : 1.0
               skarsgard = True              pos : neg    =      5.7 : 1.0
           introspective = True              pos : neg    =      5.7 : 1.0
                    tide = True              pos : neg    =      5.7 : 1.0
                  polley = True              pos : neg    =      5.7 : 1.0
                 misfire = True              neg : pos    =      5.6 : 1.0
              scratching = True              neg : pos    =      5.6 : 1.0
             ineffectual = True              neg : pos    =      5.6 : 1.0
                   piles = True              neg : pos    =      5.6 : 1.0
              simplicity = True              pos : neg    =      5.1 : 1.0
Original Naive Bayes Algo accuracy percent: 69.0
MNB_classifier accuracy percent: 72.0
BernoulliNB_classifier accuracy percent: 70.0
LogisticRegression_classifier accuracy percent: 71.0
SGDClassifier_classifier accuracy percent: 63.0
LinearSVC_classifier accuracy percent: 64.0
NuSVC_classifier accuracy percent: 71.0
voted_classifier accuracy percent: 70.0
Classification: neg Confidence %: 100.0
Classification: neg Confidence %: 57.14285714285714
Classification: pos Confidence %: 100.0
Classification: neg Confidence %: 100.0
Classification: neg Confidence %: 57.14285714285714
Classification: pos Confidence %: 100.0
```
It shows:
* Firstly, the most informative features from the training dataset. For each one, there is a statistic which shows the proportion of positive/negative appearance. In the first case, the word 'winslet' appears 9.1 times with a positive classification for each negative classification (9.1 : 1.0).
* Next, the accuracy of each classifier taking a 1,900 opinions training dataset and a 100 testing dataset is shown.
* The last part shows the ratio of votes for the classifiers as a sort of confidence indicator.
