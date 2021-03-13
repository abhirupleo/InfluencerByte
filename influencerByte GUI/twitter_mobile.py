# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:13:11 2021

@author: Jenny

Module Description:
    This module contains all the import paths for twitter data
    and also the creation of all pandas dataframe
    This file will contain all the required helper function too needed for Twitter database analyses
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from IPython.display import display

data = data = pd.read_excel('twitter_cleaned.xlsx', sheet_name='Mobile')

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
    print("\nRecommending you an influencer to market your mobile device...\n")
    twitterResultDataframe = data[data['FullTweetText'].str.contains('mobile' or 'phone')]
    m = twitterResultDataframe[twitterResultDataframe.Followers == twitterResultDataframe.Followers.max()]
    print("We recommend: ", end='')
    print(m.iloc[0]['Username'])
    print('\nThey have: ', end='')
    print(str(m.iloc[0]['Followers']), end='')
    print(' followers and ', end='')
    print(str(m.iloc[0]['TotalTweets']), end='')
    print(" total tweets.")
    

window = Tk()
window.title("TWITTER - MOBILE")
window.geometry('200x200')
header = Label(window, text="MOBILE DEVICE", font=("Britannic Bold", 18))
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