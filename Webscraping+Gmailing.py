#1. To Webscrape Stock price using Yahoo Finance and send the mail, if the particular stock value increases or decreases.
#2. Using Beautifulsoup for webscraping , SMTP to send mail.

#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import smtplib


r= requests.get('https://finance.yahoo.com/quote/TSLA?p=TSLA')
soup = BeautifulSoup(r.text, 'lxml')

def getPrice():
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    
    if float(price) < 665:
        #print("Price is low")
        sendMail()


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()      #smtp command sent by an email server to identify itself when connecting to another email server
    server.starttls()  #Security Protocol to facilitate data security over internet.
    server.ehlo()
    
    server.login('xxx@gmail.com','pwd')
    subject = 'Price Fell down for Tesla!!'
    body = 'Check the Link : https://finance.yahoo.com/quote/TSLA?p=TSLA'
    
    msg = f"Subject: {subject}\n\n{body}"
    # provide from, To and Msg
    server.sendmail(
        'xxx@gmail.com', 'xxx@gmail.com',msg
    )
    print('Mail Send!')
    server.quit()
    
        
getPrice()

