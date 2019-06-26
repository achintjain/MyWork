# -*- coding: utf-8 -*-

"""
Created on Sun May 12 12:30:50 2019

@author: achintj
"""

"""All the records corresponding to a Customer_ID on a single day will make a single transaction. 
If a transaction has 3 items {A,B,C}, then {A}, {B}, {C}, {A,B}, {B,C}, {A,C}, {A,B,C} are all 
itemsets of that transaction in which the itemsets of size 2 are {A,B}, {B,C}, {A,C}. The support 
of an itemset is the ratio of transactions in which that itemset appears to the total number of transactions. 
Write a function that for given n and p finds all the itemsets of size n with support greater than or equal to p (a fraction- 0 <p<1)"""

"""Need more time for time optimization"""

filepath = r"C:\Users\achintj\Documents\Python Scripts\CodingTest\dataSet2.csv"

with open(filepath, 'r') as f:
    results = []
    for line in f:
        words = line.split(',')
        results.append((words[0], words[1],words[2].rstrip()))

f.close()

transition_list = []

length = len(results)

def create_transactions(result_list):
    for line in result_list:
        product_list = [line2[2] for line2 in result_list if line2[0] == line[0] and line2[1] == line[1]]
        if [line[0],line[1],product_list] not in transition_list:
            transition_list.append([line[0],line[1],product_list])
    
#transition_list = [line[0],line[1],[line2[2] for line2 in tuple(results)[:100] if line2[0] == line[0] and line2[1] == line[1]] for line in tuple(results)[:100] if [line[0],line[1],[line2[2] for line2 in tuple(results)[:100] if line2[0] == line[0] and line2[1] == line[1]]] not in transition_list]

""" Taking only 50000 entries """
create_transactions(tuple(results)[:5000])

total_transitions = len(transition_list)
print(total_transitions)

def support(item_list,total_transitions,itemset):
    count = 0
    for items in item_list:
        if(all(x in items for x in itemset)):
            count += 1
    return count/total_transitions

product_sets = [item[2] for item in transition_list]
support(product_sets, total_transitions, ['10736660', '10736660', '10736660'])

def sub_lists(superlist,n): 
    for i in range(len(superlist) + 1): 
        for j in range(i + 1, len(superlist) + 1): 
            sub = superlist[i:j] 
            if len(sub)== n:
                return sub


def find_itemsets(n,p):
    semifinal_subsets = []
    final_subsets = []
    for sets in product_sets:
        sublist = sub_lists(sets,n)
        semifinal_subsets.append(sublist)
    temp = [i for i in semifinal_subsets if i] 
    for itemsets in temp:
        if itemsets not in final_subsets:
            if support(product_sets,total_transitions,itemsets) >= p:
                final_subsets.append(itemsets)
    return print(final_subsets)

"""Enter n and p below"""
find_itemsets(2,0.05)      




