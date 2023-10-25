# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:26:17 2023

@author: 林奇叡
"""

from bs4 import BeautifulSoup
import requests

url='https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
    
data=requests.get(url,headers=header).text

soup=BeautifulSoup(data,'html.parser')

rate=soup.find(id='exchangeRate')


table=rate.find('table')
tbody=table.find('tbody')
trs=tbody.find_all('tr')

for row in trs:

    tds=row.find_all('td')
    
    for rows in tds:  

        rowss=rows.text.strip()
        rowss=rowss.split()   
        if rowss==[]:
            continue
        if rowss==['銀行買入']:
            continue
        if rowss==['銀行賣出']:
            continue
        print(rowss[0])


        

          


    print('-'*80)