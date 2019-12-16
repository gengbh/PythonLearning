# -- coding: utf-8 --
import  requests
import re
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=tencent'
res = requests.get(url, headers=headers).text
# print(res)
regx='<img class="source-icon" src=(.*?) <span class="c-info">'
regx1='<p class="c-author">(.*?)</p>'
regx2='<img class="source-icon" src="(.*?)"'
regx3='<h3 class="c-title">.*?>(.*?)</a>'
text1 = re.findall(regx1, res, re.S)
# print(text1)
info = re.findall(regx2, res, re.S)
title=re.findall(regx3,res,re.S)
# print(info)
# 去除空格 和<em>
file1=open('D:\\test111.txt','a')
for i in range(len(title)):
    title[i]=title[i].strip()
    title[i]=re.sub('<.*?>','',title[i])
    file1.write(title[i]+'\n')
file1.close()
print(title)


