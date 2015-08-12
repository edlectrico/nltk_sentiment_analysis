# nltk_sentiment_analysis
Sentiment analysis algorithms applied to the NLTK movie_reviews dataset.

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
$ python3 nltk_classification.py
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

This example has been carried out following the tutorials and instructions from the Data Analysis section on [Python Programming](http://pythonprogramming.net/).
