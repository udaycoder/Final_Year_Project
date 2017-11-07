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
from nltk.tag import StanfordNERTagger

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
import urllib.request
import requests

ps = PorterStemmer()
st = StanfordNERTagger('stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'stanford-ner-2017-06-09/stanford-ner.jar',
					   encoding='utf-8')

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
    dict = {'Mountain': 'No', 'Desert': 'No', 'Waterfall': 'No', 'Beach': 'No', 'River': 'No','Workship-place': 'No','Climate': 'No','Zoo': 'No','Park': 'No','Travel': 'No','Archaeological': 'No'}

    csvfile = open("csvfile.csv", "a")
    csvfile.write("City"+','+"Mountain"+','+"Desert"+','+"Waterfall"+','+"Beach"+','+"River"+','+"Workship-place"+','+"Climate"+','+"Zoo"+','+"Park"+','+"Travel"+','+"Archaelogical-site"+','+"Rating\n")
    line=r.readline()
    while(line):
        words = nltk.word_tokenize(line)
        classified_text = st.tag(words)
        for w in classified_text:
          if w[1]=='O':
            wo=ps.stem(w[0])
            if wo in ('^'):
               city_title_full=title.readline()
               city_title=city_title_full.split('-')[0]
               new_title=list(city_title)
               new_title[len(city_title)-1]=''
               new_title=''.join(new_title)
               rating=city_title_full.split('-')[1]
               csvfile.write(new_title+','+dict['Mountain']+','+dict['Desert']+','+ dict['Waterfall']+','+dict['Beach']+','+dict['River']+','+dict['Workship-place']+','+dict['Climate']+','+dict['Zoo']+','+dict['Park']+','+dict['Travel']+','+dict['Archaeological']+','+rating)
               dict = {'Mountain': 'No', 'Desert': 'No', 'Waterfall': 'No', 'Beach': 'No', 'River': 'No','Workship-place': 'No','Climate': 'No','Zoo': 'No','Park': 'No','Travel': 'No','Archaeological': 'No'}
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
            if wo in ("Snowfall", "snowfall", "Hilly", "hilly"):
                dict['Climate'] = "Yes"
            if wo in ("Zoo", "zoo"):
                dict['Zoo'] = "Yes"
            if wo in ("Park", "park", "Garden", "garden"):
                dict['Park'] = "Yes"
            if wo in ("Airport", "airport", "Railway", "railway"):
                dict['Travel'] = "Yes"
            if wo in ("Archaeological", "archaeological"):
                dict['Archaeological'] = "Yes"    
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
         query_string=line.split('-')[0]
         corpusCreator(query_string)



#csvCreator()
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
    



