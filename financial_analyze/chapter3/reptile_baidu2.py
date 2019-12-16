# -- coding: utf-8 --
#百度爬虫代码整理
import  requests
import re
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4'
res=requests.get(url,headers=headers).text
# print(res)
#提取出新闻来源和日期
p_info='<p class="c-author">(.*?)</p>'
info = re.findall(p_info, res, re.S)
#提取新闻的网址和标题
p_href='<h3 class="c-title">.*?<a href="(.*?)"'
href=re.findall(p_href,res,re.S)
#提取标题
p_title='<h3 class="c-title">.*?>(.*?)</a>'
title=re.findall(p_title,res,re.S)



#清晰时间和来源
source=[]
date=[]
for i in range(len(info)):
    # info[i]=info[i].strip()
    info[i] = re.sub('<.*?>', '', info[i])
    source.append(info[i].split('&nbsp;&nbsp;')[0])
    date.append(info[i].split('&nbsp;&nbsp;')[1])
    source[i]=source[i].strip()
    date[i]=date[i].strip()
    title[i]=title[i].strip()
    title[i]=re.sub('<.*?>','',title[i])
    print(str(i+1)+'. '+title[i]+'('+date[i]+'-'+source[i]+')')
    print(href[i])

