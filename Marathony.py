#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:49:34 2017

@author: Ombati
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

filename= "Riadhaa.csv"
f = open(filename,"w")
for yr in range(2003,2003):
    for pg in range(1,2):
        my_url = 'https://www.iaaf.org/records/toplists/road-running/marathon/outdoor/men/senior/' + str(yr) + '?regionType=world&drop=all&fiftyPercentRule=all&page=' + str(pg)+ '&bestResultsOnly=false'
        cuClient = uReq(my_url)
        cpage_html = cuClient.read()
        cuClient.close()
        cpage_soup = soup(cpage_html, "html.parser")
        p = cpage_soup.findAll("table",{"class":"records-table"})
        len(p)
        while len(p)> 2:
           # my_url = 'https://www.iaaf.org/records/toplists/road-running/marathon/outdoor/men/senior/2018?regionType=world&drop=regular&fiftyPercentRule=regular&page=1&bestResultsOnly=false'
            uClient = uReq(my_url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")
            meza = page_soup.findAll("tr")
            n=len(meza)
            d=[]
            
            
            
            headers = "Rank,Mark,Athlete,DOB,Nat,Pos,Venue,Tarehe\n"
            f.write(headers)
            
            for i in range (0,n-1):
                d.append(meza[i].findAll("td"))
            g = len(d)
            
            for j in range (19,g-1):
                Rank = d[j][0].text.strip()
                Mark = d[j][1].text.strip()
                #Wind = d[j][2].text.strip()
                Athlete=d[j][2].text.strip()
                DOB=d[j][3].text.strip()
                Nat=d[j][4].text.strip()
                Pos=d[j][5].text.strip()
                Venue=d[j][7].text.strip()
                Tarehe=d[j][8].text.strip()
                f.write(Rank + ","+ Mark +","+ Athlete +","+ DOB+","+ Nat +","+ Pos+","+ Venue.replace(","," ") +","+ Tarehe + "\n")
                    
f.close()
