# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:27:58 2019

@author: achintj
"""

import numpy as np
from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import re

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

tfidf_vectorizer = pickle.load(open('vectorizer.pkl','rb'))

def preprocessing(userQuery):     
    letters_only = re.sub("[^a-zA-Z\\d]", " ", userQuery)
    words = letters_only.lower().split()                  
    return( " ".join(words ))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    userQuery = data['txt']
    
    userQueryList=[]
    userQueryList.append(preprocessing(userQuery))
    utfidf = tfidf_vectorizer.transform(userQueryList)
    
#    print(" prediction: ", model.predict(utfidf))
    prediction = model.predict(utfidf)
    
#    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run()

