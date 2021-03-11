# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:01:07 2021
@author: Kavyaka Pellakuru (kpellaku)

Python script to extract tweets from twitter based on a particular hashtag input
using tweepy and pandas. 
"""

# import modules 
import pandas as pd 
import tweepy   

# Function to extract tweet information for the entered search word.
def get_tweets(text_query, date_since, tweet_count): 
      
    # Creating DataFrame using pandas.
    df = pd.DataFrame(columns=['Username', 'Description', 'Location', 'Followers', 
                              'Following', 'TotalTweets', 'RetweetCount', 'DateTime', 'FullTweetText', 'Hashtags']) 
     
    '''
    Creation of query with required parameters to search through twitter for the required tweets,
    restricting the number of tweets to be extracted based on the tweet_count specified. 
   '''
    tweets = tweepy.Cursor(api.search, q=text_query, lang="en", 
                           since=date_since, tweet_mode='extended').items(tweet_count)     
         
    '''
    Iterating over the extracted list to gather below specific parameters like username,
    description, no. of followers etc.for each tweet, to analyse the top influencers.
    '''
    for tweet in tweets:
        username = tweet.user.screen_name 
        description = tweet.user.description 
        location = tweet.user.location        
        followers = tweet.user.followers_count        
        following = tweet.user.friends_count 
        totaltweets = tweet.user.statuses_count 
        retweetcount = tweet.retweet_count 
        datetime = tweet.user.created_at
        fulltweettext = tweet.full_text
        hashtags = tweet.entities['hashtags']       
        
        # Copying all the hashtags mentioned in the tweet, into a list.     
        hashtaglist = []
        for j in range(0, len(hashtags)):
            hashtaglist.append(hashtags[j]['text']) 
          
        # appending all the extracted information into the DataFrame.
        extracted_tweet_data = [username, description, location, followers, following, 
                                totaltweets, retweetcount, datetime, fulltweettext,  hashtaglist] 
        df.loc[len(df)] = extracted_tweet_data 
          
        
    filename = 'scraped_tweets.csv' 
    
    df.to_csv(filename) 
  
  
if __name__ == '__main__': 
      
    '''
    The four keys initialised below i.e, ConsumerKey, ConsumerSecret, AccessKey
    and AccessSecret are the Twitter API Keys and Tokens needed to access the twitter feed.
    '''
    consumer_key = "MLQoquNNLu7TkNIHMh0VYz6ku"
    consumer_secret = "KBaIjVXhrWpkR6ys8jpI1e8DwmmTl4oouNjppvt8Na8darotHj"
    access_key = "1363081198503796737-5llNnqhomEZkbYLOk4FHWmINyWmSPM"
    access_secret = "p11argl6swGnmcNpxdtrR0WTgdo7lfyc9SFf1d2aiD02F"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_key, access_secret) 
    api = tweepy.API(auth) 
      
    '''
    Input for hashtag search keyword and date since when the tweets should be extracted.
    Format for input: #laptop, #mobile, #tv, #smartwatch etc (input must include a # as we are extracting
    data based on the hashtags used).
    '''
    text_query = input("Enter twitter hashtag search keyword: ") 
    date_since = input("Enter date since when the tweets are required in yyyy-mm-dd format: ")    
    
    '''
    Specifying the number of tweets to be extracted.
    Limiting the search to about 300 latest tweets initially. 
    '''
    tweet_count = 300 
    get_tweets(text_query, date_since, tweet_count) 
    print('Scraping has completed!') 