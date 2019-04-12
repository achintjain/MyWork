# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:38:11 2019

@author: achintj
"""

import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'txt':'recharge my phone '})
print(r.json())