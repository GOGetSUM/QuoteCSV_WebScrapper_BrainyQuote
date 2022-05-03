#Import Statements~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import datetime as dt
import io
import random
from random import randint
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Datetime: Present State retrieval~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WeekDay_Name = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
today = dt.datetime.today().weekday()
# Returns actual present day of the week.
weekday = WeekDay_Name[today]

# Conditions: Search terms, ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#type index
scnt = 0

# Search words
SQuotes = ['technology-quotes','music-quotes','car-quotes','lifting-quotes']
SImages = ['technology','music','cars','weight lifting']
for topic in SQuotes:
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

    #Convert Quote list into a CSV file & save with todays date~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #create dictionary for panda data frame
    dict = {"Quote":quote_list,"Author":authors_list}

    #create data frame
    df = pd.DataFrame(dict)

    #save csv
    df.to_csv(f'{SQuotes[scnt]}_{weekday}')
    scnt+=1


