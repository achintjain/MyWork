# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:54:03 2019

@author: achintj
"""

"""
SCRIPT PERFORMANCE  = 18 secs
ON SYSTEM CONFIGURATION :
Processor: Intel(R) Core(TM) i7-4710HQ CPU @ 2.50GHz (8 CPUs), ~2.5GHz
Memory: 8192MB RAM
"""

filepath = r"C:\Users\achintj\Documents\Python Scripts\CodingTest\dataSet2.csv"

with open(filepath, 'r') as f:
    results = {}
    count = 0
    for line in f:
        count = count +1
        words = line.split(',')
        results[count]= {"DATE" : words[0],"CUSTOMER_ID" : words[1],"PRODUCT_ID" : [words[2].rstrip()]}

f.close()

transitions = {}

for value in results.values():
    if (value['DATE'],value['CUSTOMER_ID']) in transitions:
        transitions[(value['DATE'],value['CUSTOMER_ID'])].append(value['PRODUCT_ID'][0]) 
    else:
        transitions[(value['DATE'],value['CUSTOMER_ID'])] = value['PRODUCT_ID']

transitions.pop(('DATE','CUSTOMER_ID'))

print("****** Creating transitions *******")
print("****** Transitions Created *******")
total_transitions = len(transitions)
print("Total Transitions = ", total_transitions)

def displaysublist(masterlist):
    subcatcher = [] 
    for i in range(0,len(masterlist) + 1):   
        for j in range(i + 1, len(masterlist) + 1):         
            subcatcher.append(masterlist[i:j])
    return tuple(subcatcher)

print("****** CALCULATING ALL SUBSETS AND COUNTING THEM, WAIT FEW SECONDS ******")
subsetdict = {}
for transit in transitions.values():
    for subsets in displaysublist(transit):
        if tuple(subsets) in subsetdict.keys():
            subsetdict[tuple(subsets)] += 1
        else:
            subsetdict[tuple(subsets)] = 1

def find_itemsets(n,p):
    print("All itemsets of dimention {} and support greater than or equal to {} :".format(n,p))
    final_subsets = []
    for key,value in subsetdict.items():
        support = value/total_transitions
        if len(key) == n and support >= p:
            final_subsets.append((key,support))
    return tuple(final_subsets)

print("Finding all subsets now....")    

"""Give your n and p here"""

final_subsets = find_itemsets(2,0.005) 

for itemset,support in final_subsets:
    print("itemset = " ,list(itemset),"Support = ",support)


"""      ******TEST RESULT LOG******

****** Creating transitions *******
****** Transitions Created *******
Total Transitions =  193913
****** CALCULATING ALL SUBSETS AND COUNTING THEM, WAIT FEW SECONDS ******
Finding all subsets now....
All itemsets of dimention 2 and support greater than or equal to 0.005 :
itemset =  ['10231865', '10231865'] Support =  0.005347759046582746
itemset =  ['51540', '51540'] Support =  0.010716145900481144
itemset =  ['131467', '131467'] Support =  0.006900001547085549
itemset =  ['5701', '5702'] Support =  0.012191034123550252
itemset =  ['5701', '5701'] Support =  0.00641524807516773

"""



