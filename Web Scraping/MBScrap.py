import requests
from bs4 import BeautifulSoup
import threading

def scrapMB(fromPage,toPage):
    finalstring = ""
    for page in range(fromPage,toPage):    
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
        response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Bangalore",data)
        soup = BeautifulSoup(response.content,"html.parser")

        cards = soup.find_all("div",attrs={"class":"flex relative clearfix m-srp-card__container"})

        for card in cards[:1]:

            price = card.find("div",attrs={"class":"m-srp-card__price"})
            title = card.find("a",attrs = {"class":"m-srp-card__title"})
            super_area = card.find("div",attrs = {"class":"m-srp-card__summary__info"})
            response2 = requests.get(title.get("href"))
            soup2 = BeautifulSoup(response2.content,"html.parser")
            addr = soup2.find("div",text ="Address")
            try:
                addr_value = addr.find_next_sibling("div")
            except:
                addr_value = None
            title_text = title.text
            title_text = title.text.replace("\n","")
            title_text = title_text.replace("\t",'')
            temp = title_text.split(" ")
            for length in range(len(temp)):
                if "" in temp: temp.remove("")
            title_text = " ".join(temp)
            finalstring = finalstring + "\n {} {} {} {}".format(title_text,price.text,super_area.text,addr_value.text)
            
    fp = open("MBData.txt","a+",encoding = "utf-8")
    fp.write(finalstring)
    fp.close()
    #print(finalstring)
    

t1 = threading.Thread(target = scrapMB,args = (1,2))
t2 = threading.Thread(target = scrapMB,args = (2,3))
t3 = threading.Thread(target = scrapMB,args = (3,4))

t1.start()
t2.start()
t3.start()