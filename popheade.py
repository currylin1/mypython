# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:32:52 2023

@author: 林奇叡
"""

import requests
from bs4 import BeautifulSoup

def head():

    url='https://ak.hypergryph.com/news/2023105399.html'
    
    header={
            'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }
        
    data=requests.get(url,headers=header)
    data.encoding='utf5'
    data=data.text
    
    soup=BeautifulSoup(data,'html.parser')
    
    photo=soup.find_all('div',class_='media-wrap image-wrap')
    
    result1=[]
    
    for row in photo:
        row=row.find('img').get('src')
        result1.append(row)

    return result1
    
    
