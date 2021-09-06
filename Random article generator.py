from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser


root = Tk()
root.config(bg="#c8e0cc")
global article
article = "abc"

def get_random_article():
    try:
        global article
        global root
        url = "https://en.wikipedia.org/wiki/Special:Random"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        article = soup.find(class_ = "firstHeading").text
        title_text.config(text=article)
        root.after(1, title_text)
        return title
    except:
        return "None"

def open_wiki_url(title):
    try:
        url = 'https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
    except:
        status_text.config(text=" was not sucessful")


title_text = Label(text=article, font=("times new roman",16,"bold"), width = 60, fg="#400f00", bg="#ffcdbe")
get_random_article()

status_label = Label(text="", font=("ARIEL",15), bg="#c8e0cc")
status_text = Label(text="Do you want to read it ?", font=("Times new roman",15,"bold"), width = 30 , bg="#fffca9", fg="#003505")

my_btn1 = Button(text ="YES!!!",font=("times new roman",12,"bold"),command=lambda: open_wiki_url(article),width=10, bg="#fedffc", fg="#370133")
exit_btn = Button(root, text="EXIT",font=("times new roman",14,"bold"), command=root.destroy,bg="#ff3f08", fg="#1a0600" )
my_btn2 = Button(text ="Get another article",command=get_random_article ,font=("times new roman",15,"bold"),width=20, bg="#7bd1f8", fg="#370133")

title_text.grid(column=1,row=0,pady=10)

status_label.grid(column=0,row=1, padx=0, pady=10, sticky=W)
status_text.grid(column=1,row=1,pady=10)

my_btn1.grid(column=1,row=2,pady=5)
my_btn2.grid(column=1,row=3,pady=5)
exit_btn.grid(column=1,row=4,pady=10)

root.mainloop()