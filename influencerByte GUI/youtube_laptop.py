# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:13:11 2021

@author: abhirup

Module Description:
    This module contains all the import paths for youtube data
    and also the creation of all pandas dataframe
    This file will contain all the required helper function too needed for youtube database analyses
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from IPython.display import display

data = data = pd.read_excel('youtube_cleaned.xlsx', sheet_name='Laptop')

floatView = []
index = 0
for row in data['VIEWS']:
    if isinstance(data['VIEWS'], float):
        break
    stringValue = row[:-6] #stripping the word views from the column
    #print(stringValue)
    if stringValue.find('K') != -1: #checking if the string contains 'K' and converting it by multiplying with 10000
        #print(stringValue[:-1])
        pass
        numericValue = float(stringValue[:-1]) * 1000
        #print(round(numericValue,2))
        floatView.append(numericValue)
        data['VIEWS'][index] = numericValue
    elif stringValue.find('M') != -1: #checking if the string contains 'M' and converting it by multiplying with 1000000
        #print(stringValue[:-1])
        numericValue = float(stringValue[:-1]) * 1000000
        floatView.append(numericValue)
        #print(round(numericValue,2))
        data['VIEWS'][index] = numericValue
    elif stringValue.find('No') != -1 or stringValue.find('') != -1: #checking if the viewer had No Views then just put 0
        numericValue = 0
        data['VIEWS'][index] = numericValue
    else:
        numericValue = float(stringValue)
        data['VIEWS'][index] = numericValue            
    index += 1 #increase the index

def file_quit_click():
    window.destroy()
def help_instructions_click():
    messagebox.showinfo("HELP", "Select whether you want to scrape the data dynamically (slower) or use the pre-scraped data. Enter the market price of your prodcut and select an action")
def help_info_click():
    messagebox.showinfo("INFO", "Produced by J. Niemann, A. Panja, K. Pellakuru, D. Pandya")
def go_click():
    global dynamic
    global count
    global data
    global action2
    print("\nRecommending you an influencer to market your laptop...\n")
    influencer = data[data.VIEWS == data.VIEWS.max()]
    print("We recommend: " + influencer.iloc[0]['CHANNEL'])
    print("\nHe has total views of " + str(influencer.iloc[0]['VIEWS']) + ' on his video ' + influencer.iloc[0]['TITLE'])
    

window = Tk()
window.title("YOUTUBE - LAPTOP")
window.geometry('200x200')
header = Label(window, text="LAPTOP", font=("Britannic Bold", 18))
header.grid(column=1,row=0)

format_label = Label(window, text="             ")
format_label.grid(column=0, row=1)

menu = Menu(window)
file_item = Menu(menu)
file_item.add_command(label='Quit', command=file_quit_click)
help_item = Menu(menu)
help_item.add_command(label='Instructions', command=help_instructions_click)
help_item.add_command(label='Info', command=help_info_click)
menu.add_cascade(label='File', menu=file_item)
menu.add_cascade(label='Help', menu=help_item)

go = Button(window, text="FIND INFLUENCER", command=go_click)
go.grid(column=1, row=2)

window.config(menu=menu)

window.mainloop()