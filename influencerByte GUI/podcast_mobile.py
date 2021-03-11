# -*- coding: utf-8 -*-
"""
TEAM 7 - FINAL APPLICATION

Jennifer Niemann
Darshil Pandya
Abhirup Panja
Kavyaka Pellakuru

GUI for the podcast platform advertising for a mobile device
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

#set gloval varibles
dynamic = True
count = 0
#load the pre-scraped data for tv into a dataframe
data = data = pd.read_excel('patreon_cleaned.xls', sheet_name='Mobile')


def file_quit_click():
    window.destroy()
def help_instructions_click():
    messagebox.showinfo("HELP", "Select whether you want to scrape the data dynamically (slower) or use the pre-scraped data. Enter the market price of your prodcut and select an action")
def help_info_click():
    messagebox.showinfo("INFO", "Produced by J. Niemann, A. Panja, K. Pellakuru, D. Pandya")

#when the user selects which data method to use, set the global varible upon click
#when user chooses dynamic scraping, set dynamic to True
def data1_click():
    global dynamic
    dynamic = True
#when user chooses dynamic scraping, set dynamic to False
def data2_click():
    global dynamic
    dynamic = False
#when user selects GO, determine their selection from the dropdown menu
def go_click():
    print("\nRecommending you an influencer to market your mobile device...\n")
    global dynamic
    global count
    global data
    #if user selected dynamic scraping, run the patreon_tv file to scrape the data
    if (dynamic == True):
        print('SCRAPING DATA... please wait')
        import patreon_laptop
        exec(open('patreon_mobile.py').read())
        data = patreon_laptop.load_dataFrame()
        display(data)
        data['MONTHLY_REV'] = data['MONTHLY_REV'].astype(int) 
    global action2
    #get the user choice from the action drop down menu
    user_action = action2.get()
    if (user_action == 'Top Reccomendation'):
        #find the podcaster with the top monthly revenue
        m = data['MONTHLY_REV'].idxmax()
        print("We recommend: "+data.loc[m][0]+" they make: ", end='')
        print(data.loc[m][3], end='')
        print(" dollars a month, and have: ", end='')
        print(data.loc[m][2], end='')
        print(" subscribers")
    elif(user_action == 'View Data'):
        #display the data
        display(data)
    elif(user_action == 'View Graph'):
        data.reset_index().plot(x="PODCAST_TITLE", y=["PODCAST_SUBS", "MONTHLY_REV"], kind="bar")
        plt.title("Subscribers/Revenue per Show")
        plt.xlabel("SHOW")
        plt.show()
    elif(user_action == 'Expected Revenue'):
        #estimate an annual revenue amount from the top podcast's monthly revenue and cost of product being advertised
        global cost
        print('Expected Annual Revenue from Podcast Advertising: ')
        user_entry = cost.get()
        if (user_entry.isnumeric()):
            m = data['MONTHLY_REV'].idxmax()
            users = data.loc[m, 'PODCAST_SUBS']
            print((int(users)/10)*int(user_entry))         
        else:
            print("Enter a price for your product to calculate revenue")
    count = count + 1
     
#Tkinter Code
window = Tk()
window.title("PODCAST - MOBILE")
window.geometry('500x200')
header = Label(window, text="MOBILE", font=("Britannic Bold", 18))
header.grid(column=1,row=0)

menu = Menu(window)
file_item = Menu(menu)
file_item.add_command(label='Quit', command=file_quit_click)
help_item = Menu(menu)
help_item.add_command(label='Instructions', command=help_instructions_click)
help_item.add_command(label='Info', command=help_info_click)
menu.add_cascade(label='File', menu=file_item)
menu.add_cascade(label='Help', menu=help_item)


product_label = Label(window, text="DATA METHOD:", font=("Courier New", 12))
product_label.grid(column=0,row=1)
data1 = Radiobutton(window,text='Dynamic Scrape', value=1, command=data1_click)
data2 = Radiobutton(window,text='Pre-Scraped Data', value=2, command=data2_click)
data1.grid(column=0, row=2)
data2.grid(column=2, row=2)

cost_label = Label(window, text="COST OF PRODCUT", font=("Courier New", 12))
cost_label.grid(column=0, row=3)
cost = Entry(window)
cost.grid(column=0, row=4)

action_label = Label(window, text="SELECT ACTION:", font=("Courier New", 12))
action_label.grid(column=0,row=5)
action2 = Combobox(window)
action2['values']= ('Top Reccomendation', 'View Data', 'View Graph', 'Expected Revenue')
action2.grid(column=0, row=6)

go = Button(window, text="GO", command=go_click)
go.grid(column=1, row=7)

window.config(menu=menu)

window.mainloop()