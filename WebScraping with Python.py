#!/usr/bin/env python
# coding: utf-8

# In[54]:

#Webscraping for multiple stocks

import bs4
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

def getPrice(getLst):
    #https://finance.yahoo.com/quote/GOOGL?p=GOOGL
    r =requests.get("https://finance.yahoo.com/quote/"+ getLst + "?p=" + getLst )
    soup = BeautifulSoup(r.text, 'lxml')
    #soup
    #soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    #The above statement finds all the Div tag with class as specified.
    #[0] --> takes first index  tag with span
    price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price


lst = ['FB','GOOGL','MSFT','AMZN']
for step in range(1,100):
    price=[]
    col=[]
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    for stockcode in lst:
        price.append(getPrice(stockcode))
    col = [timestamp]
    col.extend(price)
    
    df = pd.DataFrame(col)
    #df.index=False
    df = df.T
    df.to_csv("D:\Python\RealTimeStock.csv", mode='a', header=False)
    print(col)
    
#print('The Current Price of FB : ' + str(getPrice(lst)))
