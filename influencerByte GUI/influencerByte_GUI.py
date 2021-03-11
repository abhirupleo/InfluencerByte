# -*- coding: utf-8 -*-
"""
TEAM 7 - FINAL APPLICATION

Jennifer Niemann
Darshil Pandya
Abhirup Panja
Kavyaka Pellakuru

The goal of influencerByte is to recommend marketing options to an individual customer 
for a chosen product on some of the famous marketing platforms. This is the main application
GUI where users can select the product they wish to advertise and the platform they wish to
advertise on. 
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#global variable for user product to adveritse
prod = 0;

#action on menu>file>quit click closes the application
def file_quit_click():
    window.destroy()
#action on menu>help>instructions click displays following message
def help_instructions_click():
    messagebox.showinfo("HELP", "Select the product to advertise using the radio buttons and platform to advertise on using the dropdown. Click FIND INFLUENCER to contiue.")
#action on menu>help>info click displays author information
def help_info_click():
    messagebox.showinfo("INFO", "Produced by J. Niemann, A. Panja, K. Pellakuru, D. Pandya")
#actions on raido button clicks sets the global product variable
def prod1_click():
    global prod
    prod = 1
def prod2_click():
    global prod
    prod = 2
def prod3_click():
    global prod
    prod = 3
def prod4_click():
    global prod
    prod = 4
#action on search click exectues the code that matches the user selected choices
#and opens a new GUI window for the user to interact with
def search_click():
    global prod
    plat = platform.get()
    #choices for TWITTER
    if (plat == 'Twitter'):
        if (prod == 1):
            exec(open('twitter_laptop.py').read())
        elif (prod == 2):
            exec(open('twitter_tv.py').read())
        elif (prod == 3):
            exec(open('twitter_mobile.py').read())
        elif (prod == 4):
            exec(open('twitter_watch.py').read())
        else:
            print('Select a product')
    #choices for YOUTUBE
    elif (plat == 'YouTube'):
        if (prod == 1):
            exec(open('youtube_laptop.py').read())
        elif (prod == 2):
            exec(open('youtube_tv.py').read())
        elif (prod == 3):
            exec(open('youtube_mobile.py').read())
        elif (prod == 4):
            exec(open('youtube_watch.py').read())
        else:
            print('Select a product')
    #choices for PODCASTS
    elif (plat == 'Podcasts'):
        if (prod == 1):
            exec(open('podcast_laptop.py').read())
        elif (prod == 2):
            exec(open('podcast_tv.py').read())
        elif (prod == 3):
            exec(open('podcast_mobile.py').read())
        elif (prod == 4):
            exec(open('podcast_watch.py').read())
        else:
            print('Select a product')
    else:
        print("Select a paltform")
    
#set the Tkinter window and window labels
window = Tk()
window.title("influencerByte")
window.geometry('575x200')
header = Label(window, text="influencerByte", font=("Britannic Bold", 18))
header.grid(column=1,row=0)

#set the Tkinter menu 
menu = Menu(window)
file_item = Menu(menu)
file_item.add_command(label='Quit', command=file_quit_click)
help_item = Menu(menu)
help_item.add_command(label='Instructions', command=help_instructions_click)
help_item.add_command(label='Info', command=help_info_click)
menu.add_cascade(label='File', menu=file_item)
menu.add_cascade(label='Help', menu=help_item)

#Radio buttons for the possible choices of products to advertise
product_label = Label(window, text="SELECT PRODUCT:", font=("Courier New", 12))
product_label.grid(column=0,row=2)
product1 = Radiobutton(window,text='LAPTOP', value=1, command=prod1_click)
product2  = Radiobutton(window,text='TELEVISION', value=2, command=prod2_click)
product3 = Radiobutton(window,text='MOBILE DEVICE    ', value=3, command=prod3_click)
product4 = Radiobutton(window,text='SMART WATCH', value=4, command=prod4_click)
product1.grid(column=0, row=3)
product2.grid(column=1, row=3)
product3.grid(column=2, row=3)
product4.grid(column=3, row=3)

#Drop down menu for possible choices of platforms to advertise on
platform_label = Label(window, text="SELECT PLATFORM:", font=("Courier New", 12))
platform_label.grid(column=0,row=4)
platform = Combobox(window)
platform['values']= ('Podcasts', 'Twitter', 'YouTube')
platform.grid(column=0, row=5)

#search button
search = Button(window, text="FIND INFLUENCER!", command=search_click)
search.grid(column=1, row=6)

window.config(menu=menu)

#Tkinter window runs until closed
window.mainloop()
