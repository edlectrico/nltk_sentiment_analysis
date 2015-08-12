# nltk_sentiment_analysis
Sentiment analysis algorithms applied to the NLTK movie_reviews dataset.

In this example several classification algorithms are launched. However, considering that each one has its own results (sometimes they are very different), a combination of their performance has been developed as a voting strategy.

##Tools needed and installation instructions (Ubuntu):
###1. Python
First examples have been tested with Python 2.7.9 under a Linux 64 bit architercture. However, in order to use the specific 'statistics' package, Python3 is needed. Python3 comes already with the default Ubuntu installation, so to run it on the terminal:
```
$ python3
Python 3.4.3 (default, Mar 26 2015, 22:03:40) 
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
###2. Python Pip
Pip is needed to install several packages:
```
$ sudo apt-get install python3-pip
```
###3. [NLTK](http://www.nltk.org/install.html) (Natural Language ToolKit)
It contains the necessary datasets and tools to perform text analysis within the available data. Its installation should be performed through Python:
```
$ sudo pip3 install -U nltk
```
###4. Numpy
The fundamental package for scientific computing with Python.
```
$ sudo pip3 install -U numpy
```
###5. Installing [scikit-learn](http://scikit-learn.org/stable/install.html)
It offers several tools for data mining and data analysis with Python. It requires:
```
* Python (>= 2.6 or >= 3.3),
* NumPy (>= 1.6.1),
* SciPy (>= 0.9).
 ```
- Installing dependencies for Python
```
sudo apt-get install build-essential python-dev python-setuptools \
                     python-numpy python-scipy \
                     libatlas-dev libatlas3gf-base
```
- Installing dependencies for Python3:
```
sudo apt-get install build-essential python3-dev python3-setuptools \
                     python3-numpy python3-scipy \
                     libatlas-dev libatlas3gf-base
```
- Setting ATLAS as required (only for Debian and Ubuntu distributions):
```
sudo update-alternatives --set libblas.so.3 \
    /usr/lib/atlas-base/atlas/libblas.so.3
sudo update-alternatives --set liblapack.so.3 \
    /usr/lib/atlas-base/atlas/liblapack.so.3
```
- Install matplotlib:
```
sudo apt-get install python-matplotlib
```
- And finally, install scikit-learn:
```
sudo pip install --user --install-option="--prefix=" -U scikit-learn
```
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

This example has been carried out following the tutorials and instructions from the Data Analysis section on [Python Programming](http://pythonprogramming.net/).
