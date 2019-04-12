# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:15:56 2019

@author: achintj
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from nltk.corpus import stopwords

def preprocessing(userQuery):     
    letters_only = re.sub("[^a-zA-Z\\d]", " ", userQuery)
    words = letters_only.lower().split()                  
    return( " ".join(words ))

#read utterance data from a csv file
train = pd.read_csv('Uters.csv')

query_features = train['Utterances']

tfidf_vectorizer = TfidfVectorizer(max_features=1500, stop_words=stopwords.words('english'))
new_query = [preprocessing(query) for query in query_features]
features = tfidf_vectorizer.fit_transform(new_query).toarray()

model = RandomForestClassifier(n_estimators = 100)
model.fit(features, train['Intent'])

pickle.dump(model, open('model.pkl','wb'))
pickle.dump(tfidf_vectorizer, open('vectorizer.pkl','wb'))
