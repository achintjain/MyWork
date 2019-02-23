# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:00:40 2019

@author: Achintj
"""
import requests
from bs4 import BeautifulSoup

for page in range(301,501):
    finalstring = ""
    data = {
            "propertyType_new":"10002_10003_10021_10022,10001_10017,10000",
            "city": "3327",
            "mbTrackSrc": "homeSearchForm",
            "searchType": "1",
            "propertyType": "10002,10003,10021,10022,10001,10017,10000",
            "category": "S",
            "offset": "0",
            "maxOffset": "111",
            "page": page,
            "ltrIds": "31803697,36823789,37137545,35872643,35654381,17999668,29963447,35646751,37014151,36898499,35767033,37840337,35180921,37506607,38471739,37788047,35508537,35809193,38597699,31075077,37994299,38213985,37878273,37405063,38596645,37527587,37758781,31774805,38468917,37792641"  
            }
    
    response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Bangalore",data)
    soup = BeautifulSoup(response.content,"html.parser")
    
    cards = soup.find_all("div",attrs={"class":"flex relative clearfix m-srp-card__container"})
    
    for card in cards:
        title_class = card.find("a",attrs={"class":"m-srp-card__title"})
        
        title_response = requests.get(title_class.get("href"))
        title_soup = BeautifulSoup(title_response.content,"html.parser")
        try:
            locality = title_soup.find("input",id="locality")
        except:
            locality = None
        try:
            price = title_soup.find("meta",itemprop="price")
        except:
            price = None
        try:
            bedrooms = title_soup.find("span",attrs={"class":"p_bhk"}).text
        except:
            bedrooms = None
        try:
            area = card.find("div",attrs ={"class":"m-srp-card__summary__info"}).text
        except:
            area = None
    #    print(locality.get("value"))
    #    print(price.get("content"))
    #    print(bedrooms)
    #    print(area)
        try:
            finalstring = finalstring + "{},{},{},{}".format(locality.get("value"),price.get("content"),bedrooms.replace("\n",""),area.replace("\n",""))
            finalstring = finalstring + "\n"
        except:
            pass
        
    fp = open("MBTestData.txt","a+",encoding = "utf-8")
    fp.write(finalstring)
    fp.close()
    print(finalstring)
    print("PAGE ==========================",page,"===================== ")