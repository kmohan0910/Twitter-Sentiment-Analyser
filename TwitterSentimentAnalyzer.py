import re
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from PyQt5.QtWidgets import QMessageBox

from textblob import TextBlob

from PyQt5 import QtWidgets,uic


class TwitterAnalyzer(object):
    def __init__(self):
        accessToken = '1158083326340673538-SzBqOQsUoB2rRBC7MXQJT8w9FboGue'
        accessSecretKey = 'XByBLzqP0s3arV5xsj8erfMhyGEupOY2649oZAcrROnPr'
        consumer_API_Key    =  'Cksb7KqnJDbDoTkQy2vE6bCrz'
        consumer_API_Secret =  'oElAp5ZwXE66ayEJn5McUiKjj6Wf0KOlKxRDuwFH7iXhHWuuO9'
        self.auth = OAuthHandler(consumer_API_Key, consumer_API_Secret)
        self.auth.set_access_token(accessToken, accessSecretKey)
        self.API = API(self.auth)
    def cleanTweet(self, xTweet):
        '''Using re.sub function to remove regular expression present in the Text.'''
        cleanedTweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", xTweet)
        cleanedTweet = ' '.join(cleanedTweet.split())
        return cleanedTweet

    def examineSentiments(self, xTweet):
        varAnalysis = TextBlob(self.cleanTweet(xTweet))
        if varAnalysis.sentiment.polarity > 0:
            return 'positive'
        elif varAnalysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
    def fetchTweets(self, searchAbout, varCount = 10 ): # Default Tweets to Fetch is 10
        tweets = [] # An Empty List for Storing the Parsed Tweets
        fetchedTweets = self.API.search(q = searchAbout, count = varCount)
        #print(fetchedTweets)       #TESTS
        for xTweet in fetchedTweets:
            #print(xTweet)          #TESTS
            #print(type(xTweet))
            #print(xTweet.text)   # text attribute is being used here to extract Actual Tweet from <class 'tweepy.models.Status'>
            parseTweets = {}
            parseTweets['tweets'] = xTweet.text
            parseTweets['sentiments'] = self.examineSentiments(xTweet.text)
            if xTweet.retweet_count > 0 :
                if parseTweets not in tweets:
                    tweets.append(parseTweets)
            else:
                tweets.append(parseTweets)
        return tweets

def main():
    print("\n")
    var = TwitterAnalyzer()
    searchAbout = 'Narendra Modi'
    searchAbout = call.lineEdit.text()
    varCount = call.lineEdit_2.text()
    #varcount = 20
    tweetData = var.fetchTweets(searchAbout, varCount) #List containing Dictionaries with Tweet as Key and Sentiment as Value
    #print(tweetData[0])

    positiveTweets = [tweet for tweet in tweetData if tweet['sentiments'] == 'positive']
    print("Positive tweets: {} %".format(100 * len(positiveTweets)/len(tweetData)))
    negativeTweets = [tweet for tweet in tweetData if tweet['sentiments'] == 'negative']
    print("Negative tweets: {} %".format(100 * len(negativeTweets) / len(tweetData)))
    neutralTweets  = [tweet for tweet in tweetData if tweet['sentiments'] == 'neutral']
    print("Neutral  tweets: {} %".format(100 * len(neutralTweets) / len(tweetData)))
    print("\nPositive Tweets:")
    for tweet in tweetData:
        if(tweet['sentiments']=='positive'):
            print(tweet['tweets'] + '\n')
    print("\nNegative Tweets:")
    for tweet in tweetData:
        if(tweet['sentiments']=='negative'):
            print(tweet['tweets'] + '\n')
    print("\nNeutral Tweets:")
    for tweet in tweetData:
        if (tweet['sentiments'] == 'neutral'):
            print(tweet['tweets'] + '\n')

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    call=uic.loadUi("demo.ui") # all the fuctions regarding the main window are stored in this file which is imported we can also 
                                #we can also convert ui file to py and implement in that file but that would increase the lines of code and increase the complexity.
    call.pushButton.clicked.connect(main)
    call.show()
    app.exec()