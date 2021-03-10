# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 18:09:58 2021

@author: jmnieman
"""

# from https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
import time
import xlwt 
from xlwt import Workbook 

#stitcher site to scrape
url = "https://www.stitcher.com/search/tech"

#selenium driver
d = webdriver.Chrome(executable_path=r'C:/Users/jenny/Downloads/chromedriver_win32 (2)/chromedriver.exe')
#wait for page render
d.implicetly_wait(30)
d.get(url)
SCROLL_PAUSE_TIME = 2.0

# Get scroll height
d.execute_script("window.scrollTo(0, (1000));")
#wait to render
time.sleep(SCROLL_PAUSE_TIME)

#convert selenium driver to BS object
page_source = d.page_source
bs = BeautifulSoup(page_source, 'lxml')

#open and set up excel file
#https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
wb = Workbook()
sheet1 = wb.add_sheet('Stitcher Shows')
sheet1.write(0,0,'PODCAST TITLE')
sheet1.write(0,1,'PODCAST DESCRIPTION')
row = 1

#scrape the podcast title and description
podcast_titles = bs.find_all('div', class_='text-grey5 text-truncate')
podcast_description = bs.find_all('div', class_='show-description')

#add title and description to lists
title_list = []
description_list = []

for podcast in podcast_titles:
    title = podcast.text.strip()
    title_list.append(title)
    sheet1.write(row, 0, title)
    row += 1
    
row = 1
for show in podcast_description:
   description = show.text.strip()
   description_list.append(description)
   sheet1.write(row, 1, description)
   row += 1
    
#save the excel file
wb.save('xlwt stitcher.xls')
   