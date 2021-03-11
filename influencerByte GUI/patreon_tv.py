# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:19:07 2021

@author: jmnieman
"""

from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
import time
import xlwt 
from xlwt import Workbook 
import re
import pandas as pd
from IPython.display import display

#selenium driver
d = webdriver.Chrome(executable_path=r'C:/Users/jenny/Downloads/chromedriver_win32 (2)/chromedriver.exe')
#base url to scrape
#alter query (q= ) to search for different podcasts
d.get('https://www.patreon.com/search?q=tv')

#data lists
soup_level1 = BeautifulSoup(d.page_source, 'lxml')
podcast_names = []
podcast_description = []
podcast_links = []
subscribers = []
money = []
count = 2

#get the podcast title links from the search page
for link in soup_level1.find_all('a', attrs={'href': re.compile("^https://www.patreon.com/")}):
    #for the first 10 podcasts click the link to go to the show page
    while (count <= 5):
        python_button = d.find_element_by_xpath('//*[@id="renderPageContentWrapper"]/div[1]/div/div/div['+str(count)+']/div/div[1]/a')
        if (python_button != None):
            python_button.click()    
        #convert to BS object
        soup_level2 = BeautifulSoup(d.page_source, 'lxml')
        
        #from the show page, scrape title, description, subscribers, and monthly revenue
        name = soup_level2.find('h1', class_="sc-eCssSg jjArWB")
        if (name != None):
            podcast_names.append(name.text)
        else:
            podcast_names.append(" ");
        
        description = soup_level2.find('div', class_='sc-TmcTc iXkbDO')
        if (description != None):
            podcast_description.append(description.text)
        else:
            podcast_description.append(" ")
    
        data = soup_level2.find_all('h2', class_='sc-jSgupP kIeXgk')       
        if (data != None):
            if(len(data) >= 1):
                subscribers.append(data[0].text)
            else: 
                subscribers.append(' ')
            
            if(len(data) >= 2):
                x = data[1].text.strip().replace('$', '')
                x.replace(',', '')
                print(x)
                money.append(int(x))
            else:
                money.append(0)
            
        #increment counter    
        count += 1
        
        #return to original search page
        d.execute_script("window.history.go(-1)") 
 
data_dict = {'PODCAST_TITLE': podcast_names, 'PODCAST_DESCRIPTION': podcast_description, 'PODCAST_SUBS': subscribers, 'MONTHLY_REV': money}   
data_frame = pd.DataFrame(data_dict)

def load_dataFrame():
    return data_frame
