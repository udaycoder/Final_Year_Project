#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:17:46 2018

@author: udaycoder
"""
# =============================================================================
# import re
# import nltk
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
# =============================================================================
import os
import pickle
import numpy as np
import nltk
# =============================================================================
# from nltk import word_tokenize          
# from nltk.stem import PorterStemmer
# =============================================================================

# =============================================================================
# file = open("corpus.txt","r")
# 
# document = file
# 
# document = re.sub('[^A-Za-z .-]+', ' ', str(document))
# document = document.replace('-', '')
# document = document.replace('…', '')
# document = document.replace('Mr.', 'Mr').replace('Mrs.', 'Mrs')
# 
# 
# with open("modified_corpus.txt", "w") as f1:
#     f1.write(document)
# 
# file.close()
# =============================================================================


root_dir = r"raw_en"

walker = os.walk(root_dir)

list_of_files = []

words = set(nltk.corpus.words.words())

for root,dirs,files in walker:
    for f in files:
        list_of_files.append(str(os.path.join(root,f)))
# =============================================================================
#         data = open(str(os.path.join(root,f)),"r",encoding='windows-1252')
#         content = data.read()
#         content = " ".join(w for w in nltk.wordpunct_tokenize(content) if w.lower() in words)
#         data.close()
#         data = open(str(os.path.join(root,f)),"w",encoding='utf-8')
#         data.write(content)
#         data.close()
# =============================================================================
        
    

# =============================================================================
# count_vect = CountVectorizer(input='filename', encoding='windows-1252')
# =============================================================================
        
# =============================================================================
# count_vect = pickle.load(open('cvectorizer.pkl', 'rb'))
# =============================================================================

# =============================================================================
# freq_term_matrix = count_vect.fit_transform(list_of_files)
# =============================================================================

# =============================================================================
# filename = 'cvectorizer.pkl'
# pickle.dump(count_vect , open(filename, 'wb'))
# =============================================================================

# =============================================================================
# ps = PorterStemmer()
# 
# class stemTokenizer(object):
#     def __call__(self, articles):
#         return (ps.stem(t) for t in word_tokenize(articles))
# 
# 
# tfidf = TfidfVectorizer(norm="l2",input='filename',stop_words='english',tokenizer=stemTokenizer(), lowercase = True)
# =============================================================================
 
document_file_name = ['corpus.txt']
       
# =============================================================================
# tfidf = TfidfVectorizer(norm="l2",input='filename',stop_words='english', lowercase = True)
# tfidf.fit(document_file_name)
# 
# filename = 'tfidf_ourcorpus.pkl'
# pickle.dump(tfidf , open(filename, 'wb'))
# =============================================================================

tfidf = pickle.load(open('tfidf.pkl', 'rb'))


# =============================================================================
# doc_freq_term = count_vect.transform(document_file_name)
# =============================================================================

doc_tfidf_matrix = tfidf.transform(document_file_name)

scores = zip(tfidf.get_feature_names(),
                 np.asarray(doc_tfidf_matrix.sum(axis=0)).ravel())
sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)

top_n = 20

words = set(nltk.corpus.words.words())

count = 0

attribute_file = open("attributes.txt","w")

for item in sorted_scores:
    if item[0] in words:
        if item[0]=="city":
            continue
        print("{0:50} Score: {1}".format(item[0], item[1]))
        attribute_file.write(item[0])
        attribute_file.write('\n')
        count+=1
    if count == top_n:
        break

attribute_file.close()