#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:01:37 2021

@author: Abhriup Panja
"""

"""Program Description
This program takes input from the user regarding their choice of a product
then takes an input from user regarding their preffered choice of social media. 
After processing the data, the program recommends the user an influencer fir for their
product on their preffered social media. 
"""
#importing required libs
import sys

#defining all the functions
#defining all global variables

def getInputFromUser():
    inputBoolean = True
    continueOrExit = 2
    while inputBoolean:
        try:
            continueOrExit = input("Enter your value: \n")
            continueOrExit =  int(continueOrExit)
            if continueOrExit == 1 or continueOrExit == 2:
                inputBoolean = False
            else:
                print("Please enter either 1 or 2 as your options\n")
                inputBoolean = True
        except ValueError:
            print("No valid integer! Please try again ...\n")
    if continueOrExit == 2:
        print("Thank you for using the Influencer Byte application")
        sys.exit()
    else:
        getChoiceOfProduct()    

def getChoiceOfProduct():
    inputBoolean = True
    choiceOfProduct = 5
    print("Please select a product you would like to market\n")
    print("Press 1 to choose laptops\n")
    print("Press 2 to choose mobiles\n")
    print("Press 3 to choose tvs\n")
    print("Press 4 to choose smart-watches\n")
    print("Press 5 to go to main menu\n")
    while inputBoolean:
        try:
            choiceOfProduct = input("Enter your value: \n")
            choiceOfProduct = int(choiceOfProduct)
            if choiceOfProduct > 5 or choiceOfProduct < 1:
                print("Please enter between 1-5 as your options\n")
                inputBoolean = True
            else:
                inputBoolean = False
        except ValueError:
            print("No valid integer! Please try again ...\n")
    if choiceOfProduct == 5:
        getInputFromUser()
    else:
        getChoiceOfSocialMedia(choiceOfProduct)

def getChoiceOfSocialMedia(choiceOfProduct):
    inputBoolean = True
    choiceOfSocialMedia = 5
    print("Please select a social you would like to market on\n")
    print("Press 1 to choose Youtube\n")
    print("Press 2 to choose Twitter\n")
    print("Press 3 to choose Podcast\n")
    print("Press 4 to go to choice of product\n")
    print("Press 5 to go to main menu\n")
    while inputBoolean:
        try:
            choiceOfSocialMedia = input("Enter your value: \n")
            choiceOfSocialMedia = int(choiceOfSocialMedia)
            if choiceOfSocialMedia > 5 or choiceOfSocialMedia < 1:
                print("Please enter between 1-5 as your options\n")
                inputBoolean = True
            else:
                inputBoolean = False
        except ValueError:
            print("No valid integer! Please try again ...\n")
    if choiceOfSocialMedia == 5:
        getInputFromUser()
    elif choiceOfSocialMedia == 4:
        getChoiceOfProduct()
    else:
        analyseAndRecommend(choiceOfProduct,choiceOfSocialMedia)
        
def analyseAndRecommend(choiceOfProduct,choiceOfSocialMedia):
    importModule(choiceOfSocialMedia)
    if choiceOfSocialMedia == 1:
        analyseAndRecommendYoutube(choiceOfProduct)
    elif choiceOfSocialMedia == 2:
        analyseAndRecommendYoutube(choiceOfProduct)
    elif choiceOfSocialMedia == 3:
        analyseAndRecommendYoutube(choiceOfProduct)
    
#Importing only the required module according the input of the user
def importModule(choiceOfSocialMedia):
    sys.path.insert(1, '/Users/abhirup/Documents/CMU/Data Focused Python/Group Project/InfluencerByte/modules/')
    if choiceOfSocialMedia == 1:
        global yt
        import youtubeModule as yt
    elif choiceOfSocialMedia == 2:
        global tt
        import twitterModule as tt
    elif choiceOfSocialMedia == 3:
        global pt
        import podcastModule as pt

def analyseAndRecommendYoutube(choiceOfProduct):
    if choiceOfProduct == 1:
        print("Recommending you an influencer to market your laptop\n")
        yt.convertViewsToFloat(yt.youtubeLaptopDataframe)
        print(yt.youtubeLaptopDataframe['VIEWS'].describe())
        print(yt.youtubeLaptopDataframe['VIEWS'].max())
    if choiceOfProduct == 2:
        print("Recommending you an influencer to market your mobile\n")
        yt.convertViewsToFloat(yt.youtubeMobileDataframe)
        print(yt.youtubeMobileDataframe['VIEWS'].describe())
        print(yt.youtubeMobileDataframe['VIEWS'].max())
    if choiceOfProduct == 3:
        print("Recommending you an influencer to market your tv\n")
        yt.convertViewsToFloat(yt.youtubeTvDataframe)
        print(yt.youtubeTvDataframe['VIEWS'].describe())
        print(yt.youtubeTvDataframe['VIEWS'].max())
    else:
        print("Recommending you an influencer to market your smart-watch\n")
        yt.convertViewsToFloat(yt.youtubeWatchDataframe)
        print(yt.youtubeWatchDataframe['VIEWS'].describe())  
        print(yt.youtubeWatchDataframe['VIEWS'].max())

#Printing the intro message
print("Welcome the Influencer Byte application\n")
print("***************************************\n")
print("***************************************\n")
print("Press 1 to start looking for your perfect influencer match and 2 to exit the application\n")
getInputFromUser()


    
    