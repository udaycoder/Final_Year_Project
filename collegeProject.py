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
import urllib.request
from bs4 import BeautifulSoup
import requests
import math

ps = PorterStemmer()

def corpusCreator(query_string):
    query_string=list(query_string)
    for i in range(0,len(query_string)):
        if(query_string[i]==' '):
            query_string[i]='_'
    query_string=''.join(query_string)      
    print(query_string)
    fo = open("corpus.txt", "a")
    try:
        html = urllib.request.urlopen("https://en.wikipedia.org/wiki/"+query_string).read()

        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.find_all(["p"])

        
    
        for i in soup:
            fo.write(i.get_text()+'\n')
    
        fo.write('\n')
        fo.write('^')
        fo.write('\n')
        print(query_string+" completed")
    except:
        print("EXCEPTION THROWN FOR - "+query_string+" !!!!!!")
    fo.close()
    
def csvCreator():
    r= open("corpus.txt","r")
    title=open("cities.txt","r")
    dict = {'Mountain': '0', 'Desert': '0', 'Waterfall': '0', 'Beach': '0', 'River': '0','Workship-place': '0','Climate': '0','Zoo': '0','Park': '0','Travel': '0','Archaeological': '0','Festival': '0','Pollution': '0','Tourist': '0','Cuisine': '0','Safety': '1','Museum': '0','Stadium': '0','Market': '0','Concert': '0'}

    csvfile = open("csvfile_discrete.csv", "w")
    csvfile.write("City"+','+"Mountain"+','+"Desert"+','+"Waterfall"+','+"Beach"+','+"River"+','+"Workship-place"+','+"Climate"+','+"Zoo"+','+"Park"+','+"Travel"+','+"Archaelogical-site"+','+"Festival"+','+"Pollution"+','+"Tourist"+','+"Cuisine"+','+"Safety"+','+"Museum"+','+"Stadium"+','+"Market"+','+"Concert"+','+"Rating\n")
    line=r.readline()
    while(line):
        words = nltk.word_tokenize(line)
        for w in words:
            wo=ps.stem(w)
            if wo in ('^'):
               city_title_full=title.readline()
               city_title_full=city_title_full.split('-') 
               if len(city_title_full)==2:
                   city_title=city_title_full[0]
                   city_title=list(city_title)
                   for i in range(0,len(city_title)):
                      if(city_title[i]==','):
                           city_title[i]=' '
                   city_title=''.join(city_title)
                   print(city_title,"  completed")
                   rating=float(city_title_full[1])
                   rating_floor = math.floor(float(rating))
                   rating_middle = rating_floor + 0.5;
                   rating_ceil = rating_floor + 1.0;
                   if(rating<rating_middle):
                       dis1 = abs(rating_middle-rating)
                       dis2 = abs(rating-rating_floor)
                       if(dis1<dis2):
                           rating= rating_middle
                       else:
                           rating = rating_floor
                   else:
                       dis1 = abs(rating_ceil-rating)
                       dis2 = abs(rating-rating_middle)
                       if(dis1<dis2):
                           rating= rating_ceil
                       else:
                           rating = rating_middle
               csvfile.write(city_title+','+dict['Mountain']+','+dict['Desert']+','+ dict['Waterfall']+','+dict['Beach']+','+dict['River']+','+dict['Workship-place']+','+dict['Climate']+','+dict['Zoo']+','+dict['Park']+','+dict['Travel']+','+dict['Archaeological']+','+dict['Festival']+','+dict['Pollution']+','+dict['Tourist']+','+dict['Cuisine']+','+dict['Safety']+','+dict['Museum']+','+dict['Stadium']+','+dict['Market']+','+dict['Concert']+','+str(rating)+'\n')
               dict = {'Mountain': '0', 'Desert': '0', 'Waterfall': '0', 'Beach': '0', 'River': '0','Workship-place': '0','Climate': '0','Zoo': '0','Park': '0','Travel': '0','Archaeological': '0','Festival': '0','Pollution': '0','Tourist': '0','Cuisine': '0','Safety': '1','Museum': '0','Stadium': '0','Market': '0','Concert': '0'}
            if wo in (ps.stem("Mountain"), ps.stem("mountain")):
   	           dict['Mountain'] = '1'
            if wo in (ps.stem("Desert"), ps.stem("desert")):
               dict['Desert'] = '1'
            if wo in (ps.stem("Waterfall"), ps.stem("waterfall")):
            	   dict['Waterfall'] = '1'
            if wo in (ps.stem("Beach"), ps.stem("beach"), ps.stem("beaches"), ps.stem("Beaches")):
               dict['Beach'] = '1'
            if wo in (ps.stem("River"), ps.stem("river"),ps.stem("Lake"),ps.stem("lake")):
            	   dict['River'] = '1'
            if wo in (ps.stem("Temple"), ps.stem("Church"), ps.stem("temple"), ps.stem("church"),ps.stem("Chapel"),ps.stem("chapel"),ps.stem("Mosque"),ps.stem("mosque")):
            	   dict['Workship-place'] = '1'
            if wo in (ps.stem("Snowfall"), ps.stem("snowfall"), ps.stem("Hilly"), ps.stem("hilly")):
                dict['Climate'] = '1'
            if wo in (ps.stem("Zoo"), ps.stem("zoo")):
                dict['Zoo'] = '1'
            if wo in (ps.stem("Park"), ps.stem("park"), ps.stem("Garden"), ps.stem("garden")):
                dict['Park'] = '1'
            if wo in (ps.stem("Airport"), ps.stem("airport"), ps.stem("Railway"), ps.stem("railway")):
                dict['Travel'] = '1'
            if wo in (ps.stem("Archaeological"), ps.stem("archaeological")):
                dict['Archaeological'] = '1'
            if wo in (ps.stem("Festival"), ps.stem("festival"), ps.stem("Carnival"), ps.stem("carnival"), ps.stem("Pilgrim"), ps.stem("pilgrim")):
                dict['Festival'] = '1'
            if wo in (ps.stem("Pollution"), ps.stem("pollution")):
                dict['Pollution'] = '1'
            if wo in (ps.stem("Tourist"), ps.stem("tourist")):
                dict['Tourist'] = '1'
            if wo in (ps.stem("Cuisine"), ps.stem("cuisine"), ps.stem("Food"), ps.stem("food")):
                dict['Cuisine'] = '1'
            if wo in (ps.stem("Terrorism"), ps.stem("terrorism"), ps.stem("Killing"), ps.stem("killing")):
                dict['Safety'] = '0'
            if wo in (ps.stem("Museum"), ps.stem("museum")):
                dict['Museum'] = '1' 
            if wo in (ps.stem("Stadium"), ps.stem("stadium")):
                dict['Stadium'] = '1'
            if wo in (ps.stem("Shopping"), ps.stem("shopping"), ps.stem("Market"), ps.stem("market")):
                dict['Market'] = '1'
            if wo in (ps.stem("Dance"), ps.stem("dance"), ps.stem("Music"), ps.stem("music"), ps.stem("Concert"), ps.stem("concert")):
                dict['Concert'] = '1'    
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



   









# =============================================================================
# with open("cities.txt") as f:
#       for line in f:
#          query_string=line.split('-')[0]
#          corpusCreator(query_string)
# =============================================================================




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
    



