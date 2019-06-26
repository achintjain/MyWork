# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:47 2019

@author: achintj
"""

"""1. Write a program that for a given customer_id shows the distribution of 
purchases made by that customer over different days of the week."""

filepath = r"C:\Users\achintj\Documents\Python Scripts\CodingTest\dataSet2.csv"

with open(filepath, 'r') as f:
    results = {}
    count = 0
    for line in f:
        count = count +1
        words = line.split(',')
        date = words[0].split('/')
        results[count]= {"DATE" : tuple(date),"CUSTOMER_ID" : words[1],"PRODUCT_ID" : words[2].rstrip()}

f.close()

sun= list(range(1,365,7))
mon= list(range(2,365,7))
tue= list(range(3,365,7))
wed= list(range(4,365,7))
thu= list(range(5,365,7))
fri= list(range(6,365,7))
sat= list(range(7,365,7))

fullweek = [sun,mon,tue,wed,thu,fri,sat]
fullweek_names = ['sun','mon','tue','wed','thu','fri','sat']
 
def converter(month,day):
    if month == 4:
        return day
    if month == 5:
        return 30+day
    if month == 6:
        return 30+31+day
    
def find_purchases_by_days(cust_id):
    purchases = {}
    week_data = {"sun": 0,"mon":0,"tue":0,"wed":0,"thu":0,"fri":0,"sat":0}
    week_data_dist = {"sun": 0,"mon":0,"tue":0,"wed":0,"thu":0,"fri":0,"sat":0}
    marker = '|'
    for x in range(1,len(results)+1):
        if results[x]['CUSTOMER_ID'] == cust_id:
            purchases[x] = results[x].copy()
            purchases[x].pop('CUSTOMER_ID')
            split_date = purchases[x]["DATE"]
            purchases[x]["DATE"] = {"Month":split_date[0],"Day":split_date[1],"Year":split_date[2]}
            month = purchases[x]["DATE"]["Month"]
            day = purchases[x]["DATE"]["Day"]
            converter_obj = converter(int(month),int(day))
            for index,dayslist in enumerate(fullweek):
                if converter_obj in dayslist:
                    week_data[fullweek_names[index]] += 1
    print("\n",week_data,"\n")
    total_purchases = sum(week_data.values())
    for key,values in week_data.items():
        week_data_dist[key] = str(round((values/total_purchases)*100,2)) + "%"
        print("{} : {} {}".format(key,marker*round((values/total_purchases)*100),week_data_dist[key]))

"""Enter Customer id here """    """FOLLOWING WILL GIVE USER PURCHASE ON DIFFERENT DAYS OF WEEK"""
find_purchases_by_days("102-1122432")
