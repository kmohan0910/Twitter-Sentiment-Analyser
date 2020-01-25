# twitterSentimentanalyser
It Begins with:
Authorize twitter API client.
Make a GET request to Twitter API to fetch tweets for a particular query.
Parse the tweets. Classify each tweet as positive, negative or neutral.
Tweepy: tweepy is the python client for the official Twitter API.
Install it using following pip command:
pip install tweepy
TextBlob: textblob is the python library for processing textual data.
Install it using following pip command:
pip install textblob
Also, we need to install some NLTK corpora using following command:

python -m textblob.download_corpora
(Corpora is nothing but a large and structured set of texts.)

TextBlob is actually a high level library built over top of NLTK library. First we call clean_tweet method to remove links, special characters, etc. from the tweet using some simple regex.
TextBlob uses a Movies Reviews dataset in which reviews have already been labelled as positive or negative.
Positive and negative features are extracted from each positive and negative review respectively.
Training data now consists of labelled positive and negative features. This data is trained on a Naive Bayes Classifier.
Then, we use sentiment.polarity method of TextBlob class to get the polarity of tweet between -1 to 1.





References:

http://www.ijcaonline.org/research/volume125/number3/dandrea-2015-ijca-905866.pdf
https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis
textblob.readthedocs.io/en/dev/_modules/textblob/en/sentiments.html
