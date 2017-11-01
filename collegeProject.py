# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: udaycoder
"""

import nltk
from nltk.tokenize import PunktSentenceTokenizer


from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
import urllib.request
import requests

ps = PorterStemmer()

def corpusCreator(query_string):
    query_string=list(query_string)
    for i in range(0,len(query_string)):
        if(query_string[i]==' '):
            query_string[i]='_'
    query_string=''.join(query_string)      
    print(query_string)

    html = urllib.request.urlopen("https://en.wikipedia.org/wiki/"+query_string).read()

    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.find_all(["p"])

    fo = open("corpus.txt", "a")
    
    for i in soup:
        fo.write(i.get_text()+'\n')
    
    fo.write('\n')
    fo.write('^')
    fo.write('\n')
    fo.close()
    
def csvCreator():
    r= open("corpus.txt","r")
    title=open("cities.txt","r")
    dict = {'Mountain': 'No', 'Desert': 'No', 'Waterfall': 'No', 'Beach': 'No', 'River': 'No','Workship-place': 'No'}

    csvfile = open("csvfile.csv", "a")
    line=r.readline()
    while(line):
        words = nltk.word_tokenize(line)
        for w in words:
            wo=ps.stem(w)
            if wo in ('^'):
               city_title=title.readline()
               new_title=list(city_title)
               new_title[len(city_title)-1]=''
               new_title=''.join(new_title)
               csvfile.write(new_title+','+dict['Mountain']+','+dict['Desert']+','+ dict['Waterfall']+','+dict['Beach']+','+dict['River']+','+dict['Workship-place']+',\n')
               dict = {'Mountain': 'No', 'Desert': 'No', 'Waterfall': 'No', 'Beach': 'No', 'River': 'No','Workship-place': 'No'}	   
            if wo in ("Mountain", "mountain"):
   	          dict['Mountain'] = "Yes"
            if wo in ("Desert", "desert"):
            	dict['Desert'] = "Yes"
            if wo in ("Waterfall", "waterfall"):
            	dict['Waterfall'] = "Yes"
            if wo in ("Beach", "beach", "beaches", "Beaches"):
            	dict['Beach'] = "Yes"
            if wo in ("River", "river"):
            	dict['River'] = "Yes"
            if wo in ("Temple", "Church", "temple", "church"):
            	dict['Workship-place'] = "Yes"
        line=r.readline()
           	 
    r.close()
    title.close()
    csvfile.close()
#==============================================================================
#     html1 = urllib.request.urlopen("http://www.mouthshut.com/product-reviews/Agra-reviews-925003657").read()
#     soup1 = BeautifulSoup(html1, 'html.parser')
# 
#     soup_rating = soup1.find_all("div",class_="product-rating")
# 
#     finalrating=str(soup_rating[0]['title'])
#     final_rating=finalrating.split('/')[0]
#==============================================================================



   







with open("cities.txt") as f:
     for line in f:
         query_string=line
         corpusCreator(query_string)


csvCreator()
#==============================================================================
# API_KEY = "AIzaSyAfNwA6QqnL8wJZb_quAgXf11FxxUQLTzw"
# urldetails = "https://maps.googleapis.com/maps/api/place/details/json?"
# 
# urlsearch = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
# 
# query = "foodies"
# 
# urlsearch = urlsearch + "query=" + query +"&key="+API_KEY
# 
# searchResponse = requests.post(urlsearch)
# 
# 
# 
# searchResponse=searchResponse.json()
# 
# place_id=searchResponse['results'][0]['place_id']
# 
# urldetails=urldetails+"placeid="+place_id+"&key="+API_KEY
# 
# detailsResponse=requests.post(urldetails)
# 
# detailsResponse=detailsResponse.json()
# 
# print(detailsResponse['result']['rating'])
#==============================================================================
    



