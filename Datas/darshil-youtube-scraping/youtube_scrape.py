# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 19:00:20 2021

@author: darsh
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

SEARCH = "smart+watch+reviews"
FILE_NAME = 'raw_data_watch.txt'
CHROMIUM_PATH = "C:/Program Files (x86)/chromedriver.exe"
MAIN_URL = "https://www.youtube.com/results?search_query="+SEARCH
FOUT = open(FILE_NAME, 'wt',	encoding='utf-8')

driver = webdriver.Chrome(CHROMIUM_PATH)
driver.get(MAIN_URL)

#(driver.page_source).to_csv(r'raw_data.csv', index=False)

FOUT.write(str(driver.page_source))
FOUT.close()



#navigatiing to channel page
#channelName = driver.find_element_by_xpath('.//*[@id="text"]/a')
#channelName.click

#search.send_keys(SEARCH)
#search.send_keys(Keys.RETURN)


page = driver.find_element_by_tag_name("html")
for i in range(15):
    page.send_keys(Keys.END)
    time.sleep(2)

videos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".text-wrapper.style-scope.ytd-video-renderer")))
video_list = []

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]/yt-formatted-string').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    age = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    channel = video.find_element_by_xpath('.//*[@id="channel-info"]').text
    description = video.find_element_by_xpath('.//*[@id="description-text"]').text
    #print("\n", title.strip(),"\n", channel.strip(), "\n", views.strip(), "\n", description.strip())
    vid_item = {
        'TITLE': title,
        'CHANNEL': channel,
        'VIEWS': views,
        'AGE': age,
        'DESCRIPTION': description
        }
    video_list.append(vid_item)
    #navigatiing to channel page
    #channelName = driver.find_element_by_xpath('.//*[@id="text"]/a')
    #print(channelName)
    #channelName.click
    #time.sleep(5)

#Converting to a Data Frame
df = pd.DataFrame(video_list)
#print(df)

#Exporting DF to a cdv file
df.to_csv(r'data_watch.csv', index=False)

#FOUT.write(df)
#FOUT.close()

driver.close()
