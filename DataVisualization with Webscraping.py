#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Using the WebScraped File for data visualization
#After WebScraping with Python.py do the visualization

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
%matplotlib inline

style.use('fivethirtyeight')
fig = plt.figure()

f1 = fig.add_subplot(2,2,1)
f2 = fig.add_subplot(2,2,2)
f3 = fig.add_subplot(2,2,3)
f4 = fig.add_subplot(2,2,4)

def animate(i):
    df = pd.read_csv("D:\Python\RealTimeStock.csv")
    
    ys = df.iloc[1:, 2].values
    xs = list(range(len(ys)+1))
    f1.clear()
    f1.plot(xs,ys)
    f1.set_title('FaceBook',fontsize=12)
    
    ys = df.iloc[1:, 3].values
    #xs = list(range(len(ys)+1))
    f2.clear()
    f2.plot(xs,ys)
    f2.set_title('Google',fontsize=12)
    
    ys = df.iloc[1:, 4].values
    #xs = list(range(len(ys)+1))
    f3.clear()
    f3.plot(xs,ys)
    f3.set_title('Microsoft',fontsize=12)
    
    ys = df.iloc[1:, 5].values
    #xs = list(range(len(ys)+1))
    f4.clear()
    f4.plot(xs,ys)
    f4.set_title('Amazon',fontsize=12)

ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.grid(True)
plt.tight_layout()
plt.show()
    

