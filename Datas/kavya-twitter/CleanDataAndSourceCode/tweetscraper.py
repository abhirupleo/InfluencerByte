# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:01:07 2021
@author: Kavyaka Pellakuru (kpellaku)

Python script to extract tweets based on a particular hashtag input. 
"""

# import modules 
import pandas as pd 
import tweepy 
  

# function to extract tweet information for the entered search word.
def get_tweets(text_query, date_since, tweet_count): 
      
    # Creating DataFrame using pandas 
    df = pd.DataFrame(columns=['Username', 'Description', 'Location', 'Followers', 
                              'Following', 'TotalTweets', 'RetweetCount', 'DateTime', 'FullTweetText', 'Hashtags']) 
     
    # Creation of query with required parameters to search through twitter for the required tweets. 
    
    tweets = tweepy.Cursor(api.search, q=text_query, lang="en", 
                           since=date_since, tweet_mode='extended').items(tweet_count) 
    
    #tweets_list = [tweet for tweet in tweets] 
      
     
    # iterating over each tweet in the list for extracting information about each tweet 
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
        
             
        hashtaglist = []
        for j in range(0, len(hashtags)):
            hashtaglist.append(hashtags[j]['text']) 
          
        # appending all the extracted information into the DataFrame 
        extracted_tweet_data = [username, description, location, followers, following, 
                                totaltweets, retweetcount, datetime, fulltweettext,  hashtaglist] 
        df.loc[len(df)] = extracted_tweet_data 
          
        
    filename = 'scraped_tweets.csv'  
    
    df.to_csv(filename) 
  
  
if __name__ == '__main__': 
      
    # Twitter API Keys
    consumer_key = "MLQoquNNLu7TkNIHMh0VYz6ku"
    consumer_secret = "KBaIjVXhrWpkR6ys8jpI1e8DwmmTl4oouNjppvt8Na8darotHj"
    access_key = "1363081198503796737-5llNnqhomEZkbYLOk4FHWmINyWmSPM"
    access_secret = "p11argl6swGnmcNpxdtrR0WTgdo7lfyc9SFf1d2aiD02F"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_key, access_secret) 
    api = tweepy.API(auth) 
      
    # Input for hashtag search word 
    #format to input - #laptop #mobile #tv #smartwatch etc (input should include a #)
    text_query = input("Enter twitter hashtag search keyword: ") 
    date_since = input("Enter date since when the tweets are required in yyyy-mm-dd format: ")    
    # Specifying the number of tweets to be extracted. 
    tweet_count = 300 
    get_tweets(text_query, date_since, tweet_count) 
    print('Scraping has completed!') 