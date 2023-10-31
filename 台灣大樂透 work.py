# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:35:08 2023

@author: 林奇叡
"""

import requests
from bs4 import BeautifulSoup

url='https://www.taiwanlottery.com.tw/result_all.htm'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }  
    
    
data=requests.get(url)
data.encoding='utf-8'
data=data.text
soup=BeautifulSoup(data,'html.parser')

dd=soup.find(id='right_full')

picture=dd.find_all('img')

# for p in picture:
#     p=p.get('src')
#     p='https://www.taiwanlottery.com.tw/'+p
#     print('運彩各種圖',p)

table=soup.find_all('table',class_='tableWin')

i=-1
for t in table:
    t=t.find_all('tr')
    ts=t[0].text.split()
    i+=1

    print(ts[1])
    number=t[4].find_all('span')
    nn=[]
    for n in number:
        n=n.text.split()
        
        if ts[1]=='3星彩':
            n=n[0]           
            nn.append(n)
        
        
        if n not in nn:
            n=n[0]
            if n not in nn:            
                nn.append(n)
                
    if ts[1]=='威力彩':
        nnp=nn.pop(6)
        print('特別號碼',nnp) 
    if ts[1]=='大樂透':
        nnp=nn.pop(6)
        print('特別號碼',nnp)       
    print(nn,end=',')
    print()
    print('圖片:','https://www.taiwanlottery.com.tw/'+picture[i].get('src'))
    print()                 
    print('-'*100)