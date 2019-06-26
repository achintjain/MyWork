# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:42:38 2019

@author: achintj
"""

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\achintj\Documents\Python Scripts\CodingTest\dataSet2.csv")

transition = data.groupby(["CUSTOMER_ID","DATE"])

def displaysublist(masterlist,n):
    subcatcher = [] 
    for i in range(0,len(masterlist) + 1):   
        for j in range(i + 1, len(masterlist) + 1):         
            sub = masterlist[i:j]
            if len(sub) == n:
                subcatcher.append(sub) 
    return tuple(subcatcher)

def support(itemset,transition_product_list,total_transitions):
    itemset_count = 0
    for items in transition_product_list:
        if all(elem in items for elem in itemset):
            itemset_count += 1
    return itemset_count/total_transitions

transition_product_list = np.array([tuple(transition.get_group(name)["PRODUCT_ID"]) for name,groups in transition])
total_transitions = len(transition_product_list)
support((5701,5702),transition_product_list,total_transitions)

def find_itemsets(n,p):
    transition_product_list = np.array([tuple(transition.get_group(name)["PRODUCT_ID"]) for name,groups in transition])
    total_transitions = len(transition_product_list)
    print("Total Transitions = ",total_transitions)
    itemsets = []
    count = 0
    for item in transition_product_list:
        count = count + 1
        print(count,"/ 193913")
        for fetched in tuple(displaysublist(item,n)):
            local_support = support(fetched,transition_product_list,total_transitions)
            if local_support >= p and fetched not in itemsets:
                itemsets.append((fetched))
                print(local_support)
    return print(tuple(itemsets))


find_itemsets(3,0.005)
