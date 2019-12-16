# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup
import re

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url='https://news.sogou.com/news?ie=utf8&p=40230447&interV=kKIOkrELjboMmLkEkL0TkKIMkLELjbcLmLkElbcTkKIRmLkElbYTkKIKmbELjbkRmLkEk78TkKILkbHjMz+PEl+XJ6IPjeh5yuF9j/lHxOVNj+lHzrGIAEbHEkOILqIPjedEyuh5w+cGwOVFmUHpGHIElKJLzO5Nj+lHzo==_-1030582931&query=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&'
res = requests.get(url, headers=headers, timeout=10).text
# print(res)
soup=BeautifulSoup(res,'html.parser')
# for i in soup.select('h3[class="vrTitle"]'):
#     # print(i)
#     print(i.a.attrs['href'])
#     print(i.a.text)
source=[]
date=[]
href=[]
title=[]
for i in soup.select('div[class="vrwrap"]'):
    # print(i)
    #解析url title
    j=i.select('h3[class="vrTitle"]')
    for m in j:
        href=m.a.attrs['href']
        title = m.a.text
        print(title+ '\n'+href)
    #解析时间 来源
    for n in i.select('div[class="news-info"]'):
       for mmm in n.select('p[class="news-from"]'):
        s=mmm.text.split(' ')[0]
        d=mmm.text.split(' ')[1]

        print(s+'---'+d)

# a = [1,2]

# b = [2,3]
# import pandas as pd

# print()

