# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:14:52 2023

@author: USER
"""
import json
import requests
from bs4 import BeautifulSoup
import csv

url='https://www.thsrc.com.tw/TimeTable/Search'

header={
        'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }  
    
thrsunfo={'台北':'TaiPei','南港':'NanGang','板橋':'BanQiao','桃園':'TaoYuan','新竹':'XinZhu'}
print('車站:',thrsunfo.keys())
gostation=input('出發站:')
endstation=input('抵達站')
gotime=input('出發時間:')
go = thrsunfo.get(gostation,'NanGang')  #get 加預設值
end=thrsunfo.get(endstation,'ZuoYing') 


    
param={
       'SearchType': 'S',
'Lang': 'TW',
'StartStation': go,
'EndStation': end,
'OutWardSearchDate': '2023/10/30',
'OutWardSearchTime': gotime,
'ReturnSearchDate': '2023/10/30',
'ReturnSearchTime': '21:00',

       }

data=requests.post(url,data=param,headers=header).text

thsrc=json.loads(data)
items=thsrc['data']['DepartureTable']['TrainItem']

fileName='thrsc.csv'
fObj=open(fileName,'w',newline='')
csvWrite=csv.writer(fObj)
csvWrite.writerow(['車次','出發時間','抵達時間','旅行時間','停靠站'])


for row in items:
    if row['DepartureTime'] >=gotime:
        
        print(row['TrainNumber'])
        print(row['DepartureTime'])
        print(row['DestinationTime'])
        print(row['Duration'])
        station=row['StationInfo']
        print('停靠站:',end='')
        msg=''
        for s in station:
            if s['Show']:
                print(s['StationName'],end=',')
                msg+=s['StationName']+','
        print()
                
        print('-'*60)
        csvWrite.writerow([row['TrainNumber'],row['DepartureTime'],row['DestinationTime'],row['Duration'],msg])
        
fObj.close()
    
    
    
#1.各站停靠站  2.輸入站名出現時間 param  3.出現今天時間之後的班別