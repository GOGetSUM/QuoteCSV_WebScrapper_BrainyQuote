#Import Statements~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import datetime as dt
import io
import random
from random import randint

import numpy
import requests
from bs4 import BeautifulSoup
import os
from scipy import misc
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random

#Datetime: Present State retrieval~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WeekDay_Name = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
today = dt.datetime.today().weekday()
# Returns actual present day of the week.
weekday = WeekDay_Name[today]


# Conditions: Search terms, ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#type index
scnt = 0

# Search words
SQuotes = ['technology-quotes']
SImages = ['technology']
# File names
FName_img = [f'{SImages[scnt]}_{weekday}']


#API Keys:
SK = "26625580-44ea7ddb93146dc5574c3bdff" # pixabay key account

#QUOTE - Retrival~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Site to be scrubbed.
SITE = f"https://www.brainyquote.com/topics/{SQuotes[scnt]}"

#request to get site through module "requests"
response = requests.get(SITE)
print(response)

quote_html = response.text

#html text needs to be parse through Beautiful Soup, create some soup.
soup = BeautifulSoup(quote_html,'html.parser')

#Quotes
# Define handle for element in htlm needed and retrieve, I retrieved all quotes from search
quotes = soup.select(selector="a div")

# Create list of quotes from soup of all quotes, add to list
quote_list = []
for quote in quotes:
    text = quote.text.strip('\n').format()
    quote_list.append(text)

#Author
# Define handle for element in htlm needed and retrieve, I retrieved all authors from search
authors = soup.find_all(title='view author') #element handle corresponed to quotes, will match in list index
# Create list of all authors
authors_list = []
for author in authors:
    text2 = author.text
    authors_list.append(text2)

#Quote-Formatting~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
format_notdone = True #formatting section will run until formattign complete

while format_notdone:
    chosen_index = randint(0,len(quote_list)-1) #need to be pull to use same value on both quote & author
    #retrieve given text for quote
    chosen_qte = quote_list[chosen_index]
    chosen_author = authors_list[chosen_index]
    #Attempt at wrapping function
    if len(chosen_qte)<500: # condition on max characters allowed
        chosen_formatted = ""
        for i, letter in enumerate(chosen_qte):
            if i % 14 == 0  and letter == " ":
                chosen_formatted += '\n'
            elif i % 16 == 0 and letter == " ":
                chosen_formatted += '\n'
            elif  i % 18 == 0 and letter==" ":
                chosen_formatted += '\n'
            chosen_formatted += letter
        format_notdone = False
    else:
        pass
#Images - Retrieval, saving and formatting
Img_site = 'https://pixabay.com/api/'     # pixabay.com api site
img_endpoint = f"{Img_site}/?key={SK}&q={SImages[scnt]}&image_type=photo" # included headers for get request to come

#GET - requests
response = requests.get(url=img_endpoint)
img_search = response.json() #turn response in json.
img_data = img_search['hits']  #based on json structure we only need the hits section

#Create img list from data - url only
url_list = []
for hit in img_data:
    url = hit['largeImageURL']
    url_list.append(url)
print(f'Image Url list completed, total number of hits:{len(url_list)}')

#Chose a random image and save under its file name
img_num = randint(0,len(url_list)-1)
img_url = url_list[img_num]
#
# requesting actual image and saving from src url
img = requests.get(img_url)
f_ext = os.path.splitext(f'{img_url}')[-1] #
f_name = f'{FName_img[scnt]}.png' # File path and file name of image file



# with open(f_name,'wb') as f_image:   #built-in function open will open file and truncate
#     f_image.write(img.content)
#
#
# #creating a version of the file as black and white
# with open(f_name,'wb') as f_image_bw:   # similar to above, this version will be manipulated
#     f_image_bw.write(img.content)
#
# f_image_bw = numpy.fromstring()
#
#
#
# #Tk - window creator~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



