#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:26:15 2021

@author: abhirup
"""

"""
Module Description:
    This module contains all the import paths for youtube data
    and also the creation of all pandas dataframe
    This file will contain all the required helper function too needed for youtube database analyses
"""
#importing the required libraries
import pandas as pd

path_youtube_laptop = "Datas/darshil-youtube-scraping/data_laptop.csv" #Path to the data for Youtube laptop specific videos
path_youtube_mobile = "Datas/darshil-youtube-scraping/data_mobile.csv" #Path to the data for Youtube mobile specific videos
path_youtube_tv = "Datas/darshil-youtube-scraping/data_tv.csv" #Path to the data for Youtube tv specific videos
path_youtube_watch = "Datas/darshil-youtube-scraping/data_watch.csv" #Path to the data for Youtube watch specific videos

#Defining the Dataframes for Youtube
youtubeLaptopDataframe = pd.read_csv(path_youtube_laptop) #reading the youtube laptop data into a pandas dataframe
youtubeMobileDataframe = pd.read_csv(path_youtube_mobile) #reading the youtube mobile data into a pandas dataframe
youtubeTvDataframe = pd.read_csv(path_youtube_tv)         #reading the youtube tv data into a pandas dataframe
youtubeWatchDataframe = pd.read_csv(path_youtube_watch)   #reading the youtube watch data into a pandas dataframe

"""
convertViewsToFloat(dataFrame)
This function converts the views column of the youtube dataframe which is in strings to float
in: name of the dataframe
out: view column of the dataframe will be converted and replaced into float
"""
def convertViewsToFloat(dataFrame):
    floatView = []
    index = 0
    for row in dataFrame['VIEWS']:
        if isinstance(dataFrame['VIEWS'], float):
            break
        stringValue = row[:-6] #stripping the word views from the column
        #print(stringValue)
        if stringValue.find('K') != -1: #checking if the string contains 'K' and converting it by multiplying with 10000
            #print(stringValue[:-1])
            pass
            numericValue = float(stringValue[:-1]) * 1000
            #print(round(numericValue,2))
            floatView.append(numericValue)
            dataFrame['VIEWS'][index] = numericValue
        elif stringValue.find('M') != -1: #checking if the string contains 'M' and converting it by multiplying with 1000000
            #print(stringValue[:-1])
            numericValue = float(stringValue[:-1]) * 1000000
            floatView.append(numericValue)
            #print(round(numericValue,2))
            dataFrame['VIEWS'][index] = numericValue
        elif stringValue.find('No') != -1 or stringValue.find('') != -1: #checking if the viewer had No Views then just put 0
            numericValue = 0
            dataFrame['VIEWS'][index] = numericValue
        else:
            numericValue = float(stringValue)
            dataFrame['VIEWS'][index] = numericValue            
        index += 1 #increase the index