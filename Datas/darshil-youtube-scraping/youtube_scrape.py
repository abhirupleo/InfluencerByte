# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:00:20 2021

@author: darsh
"""
'''Importing the relevant modules to run the program'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


SEARCH = "smart+watch+reviews"                                          #search string
FILE_NAME = 'raw_data_watch.txt'                                        #file that stores html of the page
CHROMIUM_PATH = "C:/Program Files (x86)/chromedriver.exe"               #chromium path to run selenium from
MAIN_URL = "https://www.youtube.com/results?search_query="+SEARCH       #youtube link to search the data

FOUT = open(FILE_NAME, 'wt',	encoding='utf-8')                          #opening file

#initializing and running chromium driver using webdriver from seleium
driver = webdriver.Chrome(CHROMIUM_PATH)            
driver.get(MAIN_URL)

#writing html of page to file
FOUT.write(str(driver.page_source))
FOUT.close()

'''
Code snippet for scrolling down the page 15 times. 
We do this to obtain a good quantity of data to scrape.
'''
page = driver.find_element_by_tag_name("html")
for i in range(15):
    page.send_keys(Keys.END)
    time.sleep(2)

'''
Storing all the video tages in videos
'''
videos = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-wrapper.style-scope.ytd-video-renderer")))
video_list = []

'''
The for loops iterates through all the individual videos loaded on the search page
'''
for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]/yt-formatted-string').text    #Storing the video title'''
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text              #Storing the video views'''
    age = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text                #Storing the video age'''
    channel = video.find_element_by_xpath('.//*[@id="channel-info"]').text                     #Storing the video channel name'''
    description = video.find_element_by_xpath('.//*[@id="description-text"]').text             #Storing the video description'''
    
    '''
    Creating a vid_item dictionary.
    '''
    vid_item = {
        'TITLE': title,
        'CHANNEL': channel,
        'VIEWS': views,
        'AGE': age,
        'DESCRIPTION': description,
        }
    video_list.append(vid_item)


#Converting to a Data Frame
df = pd.DataFrame(video_list)

#Exporting DF to a cdv file
df.to_csv(r'data_watch.csv', index=False)

#closing the browser window
driver.close()
