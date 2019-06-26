# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:54:03 2019

@author: achintj
"""

"""
SCRIPT PERFORMANCE  = 2 MINUTE 05s 72 
ON SYSTEM CONFIGURATION :
Processor: Intel(R) Core(TM) i7-4710HQ CPU @ 2.50GHz (8 CPUs), ~2.5GHz
Memory: 8192MB RAM
"""

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\achintj\Documents\Python Scripts\CodingTest\dataSet2.csv")
transition = data.groupby(["CUSTOMER_ID","DATE"])
print("****** WAIT FEW MINUTES, THIS IS NOT A HANG ******")
print("****** Creating transitions !! This might take 1 to 5 minutes ******")
transition_product_list = np.array([tuple(transition.get_group(name)["PRODUCT_ID"]) for name,groups in transition])
print("****** Transitions Created")
total_transitions = len(transition_product_list)
print("Total Transitions = ", total_transitions)

def displaysublist(masterlist):
    subcatcher = [] 
    for i in range(0,len(masterlist) + 1):   
        for j in range(i + 1, len(masterlist) + 1):         
            subcatcher.append(masterlist[i:j])
    return tuple(subcatcher)

print("****** CALCULATING ALL SUBSETS AND COUNTING THEM, WAIT FEW SECONDS ******")
subsetdict = {}
for transit in transition_product_list:
    for subsets in displaysublist(transit):
        if subsets in subsetdict.keys():
            subsetdict[subsets] += 1
        else:
            subsetdict[subsets] = 1

subsetdict

def find_subsets(n,p):
    print("All itemsets of dimention {} and support greater than or equal to {} :".format(n,p))
    final_subsets = []
    for key,value in subsetdict.items():
        support = value/total_transitions
        if len(key) == n and support >= p:
            final_subsets.append((key,support))
#            print(key,value,support)
    return tuple(final_subsets)

print("Finding all subsets now....")    

"""Give your n and p here"""
final_subsets = find_subsets(2,0.005) 

for itemset,support in final_subsets:
    print("itemset = " ,list(itemset),"Support = ",support)


"""      ******RESULT LOG******

****** WAIT FEW MINUTES, THIS IS NOT A HANG ******
****** Creating transitions !! This might take 1 to 5 minutes ******
****** Transitions Created
Total Transitions =  193913
****** CALCULATING ALL SUBSETS AND COUNTING THEM, WAIT FEW SECONDS ******
Finding all subsets now....
All itemsets of dimention 2 and support greater than or equal to 0.005 :
[131467, 131467] 0.006900001547085549
[51540, 51540] 0.010716145900481144
[5701, 5701] 0.00641524807516773
[5701, 5702] 0.012191034123550252
[10231865, 10231865] 0.005347759046582746


"""



