#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: udaycoder
"""

import nltk
#from nltk.tokenize import PunktSentenceTokenizer
#from nltk.tag import StanfordNERTagger
#from nltk.stem import WordNetLemmatizer
#from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
import urllib.request
from bs4 import BeautifulSoup
#import requests

ps = PorterStemmer()
# =============================================================================
# st = StanfordNERTagger('stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
# 					   'stanford-ner-2017-06-09/stanford-ner.jar',
# 					   encoding='utf-8')
# =============================================================================

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
    attributes = open("attributes.txt","r")
    
    dict = {}
    list_of_attributes = []
    one_attribute = attributes.readline()
    
    csvTitle=[]
    csvTitle.append("City")
    csvTitle.append(',')
    while(one_attribute):
        one_attribute = one_attribute.strip('\n')
        list_of_attributes.append(one_attribute)
        csvTitle.append(one_attribute)
        dict.update({one_attribute:'No'})
        one_attribute = attributes.readline()
        if(one_attribute):
            csvTitle.append(',')
    
    csvTitle.append(',')
    csvTitle.append("Rating")
    csvTitle.append('\n')
    
    csvTitleStr = ''.join(csvTitle)
    
    attributes.close()    

    csvfile = open("csvfile.csv", "w")
    csvfile.write(csvTitleStr)
    
    line=r.readline()
    while(line):
        words = nltk.word_tokenize(line)
        #classified_text = st.tag(words)
        for w in words:
          #if w[1]=='O' and (w[0]!=''):
            #wo=ps.stem(w[0])
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
                   rating=city_title_full[1]
                   
               one_csv_line = []
               one_csv_line.append(city_title)
               for key,value in dict.items():
                   one_csv_line.append(',')
                   one_csv_line.append(value)
               one_csv_line.append(',')
               one_csv_line.append(rating)
               #one_csv_line.append('\n')
               one_csv_line_str = ''.join(one_csv_line)
               csvfile.write(one_csv_line_str)
               for key,value in dict.items():
                          dict.update({key:'No'})
                          
            for x in list_of_attributes:
                if wo.lower() in ps.stem(x):
                    dict[x] = 'Yes'
                    
            
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
    



