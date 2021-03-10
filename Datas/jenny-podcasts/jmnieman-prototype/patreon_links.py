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

#selenium driver
d = webdriver.Chrome(executable_path=r'C:/Users/jenny/Downloads/chromedriver_win32 (2)/chromedriver.exe')
#base url to scrape
d.get('https://www.patreon.com/search?q=dev')

#data lists
soup_level1 = BeautifulSoup(d.page_source, 'lxml')
podcast_names = []
podcast_description = []
podcast_links = []
subscribers = []
money = []
count = 2

#set up excel sheet 
wb = Workbook()
sheet1 = wb.add_sheet('Patreon Shows')
sheet1.write(0,0,'PODCAST TITLE')
sheet1.write(0,1,'PODCAST DESCRIPTION')
sheet1.write(0,2, 'PODCAST SUBS')
sheet1.write(0,3, 'MONTHLY REV')
row = 1


#get the podcast title links from the search page
for link in soup_level1.find_all('a', attrs={'href': re.compile("^https://www.patreon.com/")}):
    #for the first 10 podcasts click the link to go to the show page
    while (count <= 10):
        python_button = d.find_element_by_xpath('//*[@id="renderPageContentWrapper"]/div[1]/div/div/div['+str(count)+']/div/div[1]/a')
        if (python_button != None):
            python_button.click()    
        #convert to BS object
        soup_level2 = BeautifulSoup(d.page_source, 'lxml')
        
        #from the show page, scrape title, description, subscribers, and monthly revenue
        name = soup_level2.find('h1', class_="sc-AxhUy iYEgas")
        if (name != None):
            podcast_names.append(name.text)
        else:
            podcast_names.append("-");
        
        description = soup_level2.find('div', class_='sc-1sp3zau-0 eZXWbx')
        if (description != None):
            podcast_description.append(description.text)
        else:
            podcast_description.append("-")
    
        data = soup_level2.find_all('h2', class_='sc-AxgMl kHusHC')       
        if (data != None):
            if(len(data) >= 1):
                subscribers.append(data[0].text)
            else: 
                subscribers.append('-')
            
            if(len(data) >= 2):
                money.append(data[1].text)
            else:
                money.append('-')
            
        #increment counter    
        count += 1
        
        #return to original search page
        d.execute_script("window.history.go(-1)") 
    

#write the informationt to excel sheet
for x in range(0, len(podcast_names)):
    sheet1.write(row, 0, podcast_names[x])
    sheet1.write(row, 1, podcast_description[x])
    sheet1.write(row, 2, subscribers[x])
    sheet1.write(row, 3, money[x])
    row += 1

#save the excel file
wb.save('xlwt patreon6.xls')
