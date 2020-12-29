#!/usr/bin/env python
# coding: utf-8

# In[49]:

#Real Time Stock Data Analysis with Python
#1. Get the Stock Analysis API.
#	>> pip3 install alpha-vantage	
#2. Get the alpha-vantage API Key. (https://www.alphavantage.co/)
#	>> Welcome to Alpha Vantage! Your API key is: MHP068BZNTQ23MKI. Please record this API key at a safe place for future data access.	
#3.	Write the Python code in Jupyter or pycharm.

import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import datetime
import time

API_KEY = 'MHP068BZNTQ23MKI'
ts = TimeSeries(key=API_KEY, output_format='pandas')

def getPrice():
    df, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
    data = df.sort_values('date')
    
    data, meta_data = ts.get_intraday(symbol=itms, interval='1min', outputsize='full')
    data.to_excel("D:\Python\MSFTStocks.xlsx")
    time.sleep(60)
    print(data)

getPrice()

## look for closing value if the value is > 0.0004
##closing_value = data['4. close']
##Last_change = closing_value.pct_change()
##if abs(Last_change[-1])> 0.0003:
##    print('MS Alert : ' , Last_change[-1] )
