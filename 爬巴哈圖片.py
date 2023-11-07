# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:37:26 2023

@author: 林奇叡
"""

import requests
from bs4 import BeautifulSoup
import os

url='https://forum.gamer.com.tw/B.php?page=1&bsn=33651'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
'Cookie':
'nologinuser=019c86406d93e0634fc8a12c4da2b64b7f41327fc342034b65326f903126; ckM=2095055395; _ga_MT7EZECMKQ=GS1.1.1697811109.2.0.1697811109.60.0.0; ckFORUM_bsn=33651; ckBahaAd=----------------0--------; ckBH_lastBoard=[[%2233651%22%2C%22%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F%22]]; buap_modr=p019; buap_puoo=p402%20p401%20p101; _gid=GA1.3.589502488.1699153111; __cf_bm=UHpr8Sa3aaouRPy47Zu3PXvO_a81gJ3qY1J77O2qpY8-1699155343-0-AbOo8N6/oBXf3OxAo4Hp1eHxrq4O8kysYurB/t2D2JPBgqyEDp9dvRm2nxB/8c4Cy2LOsL7mgFEyjp0enww5NhA=; __gads=ID=228c2c6d187cc2fb:T=1693668630:RT=1699155710:S=ALNI_MYgK_5KQEHtIEC6kSzxdISJFfNrIg; __gpi=UID=00000c39c31eb778:T=1693668630:RT=1699155710:S=ALNI_MZnJA16hABoHOS7O8kSTGDQigjdQg; _ga=GA1.1.588056014.1693668626; _ga_2Q21791Y9D=GS1.1.1699153131.5.1.1699155858.60.0.0'
        }
a=0
g=0
picture='picture1'
if not os.path.exists(picture):
    os.makedirs(picture)

for b in range(2):
    url='https://forum.gamer.com.tw/B.php?page='+str(a)+'&bsn=33651'    
    data=requests.get(url,headers=header).text
    soup=BeautifulSoup(data,'html.parser')
    title=soup.find_all('div',class_='b-list__tile')
    
    for t in title:
        try:
            
            tt=t.find('p').text
            link='https://forum.gamer.com.tw/'+t.find('p').get('href')
            # print(link)
            # print(tt)
            
            # print('-'*100)
            if '繪圖' in tt:
                url2=link
                data=requests.get(url2,headers=header).text
                soup=BeautifulSoup(data,'html.parser')
                title=soup.find('div',class_='c-post__body')
                photo=title.find('img').get('data-src')
                print(photo)
                w=requests.get(photo)
                
                filename='C:\\Users\m0050\OneDrive\桌面\\自我爬蟲\picture1\\'+str(g)+'.jpg'
                with open(filename,'wb') as obj:
                    obj.write(w.content)
                    g+=1
                

        except AttributeError :
            print('None')

            
            

        
        
    a+=1
    
