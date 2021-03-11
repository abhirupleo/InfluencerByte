#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:08:14 2021

@author: abhirup
"""

"""
Module Description:
    This module contains all the import paths for twitter data
    and also the creation of all pandas dataframe
"""

#importing the required libraries
import pandas as pd

path_twitter_laptop = "../Datas/kavya-twitter/CleanDataAndSourceCode/laptop_scraped_tweets.csv" #Path to the data for Twitter for laptop
path_twitter_mobile = "../Datas/kavya-twitter/CleanDataAndSourceCode/mobile_scraped_tweets.csv" #Path to the data for Twitter for mobile
path_twitter_tv = "../Datas/kavya-twitter/CleanDataAndSourceCode/tv_scraped_tweets.csv" #Path to the data for Twitter for tv
path_twitter_watch = "../Datas/kavya-twitter/CleanDataAndSourceCode/smartwatch_scraped_tweets.csv" #Path to the data for Twitter for watch

#Defining the Dataframes for Twitter
twitterLaptopDataframe = pd.read_csv(path_twitter_laptop) #reading the twitter laptop data into a pandas dataframe
twitterMobileDataframe = pd.read_csv(path_twitter_mobile) #reading the twitter mobile data into a pandas dataframe
twitterTVDataframe = pd.read_csv(path_twitter_tv)         #reading the twitter tv data into a pandas dataframe
twitterWatchDataframe = pd.read_csv(path_twitter_watch)   #reading the twitter watch data into a pandas dataframe

