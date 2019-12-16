# -- coding: utf-8 --
import requests
from bs4 import BeautifulSoup
import re

headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url='https://news.sogou.com/news?ie=utf8&p=40230447&interV=kKIOkrELjboMmLkEkL0TkKIMkLELjbcLmLkElbcTkKIRmLkElbYTkKIKmbELjbkRmLkEk78TkKILkbHjMz+PEl+XJ6IPjeh5yuF9j/lHxOVNj+lHzrGIAEbHEkOILqIPjedEyuh5w+cGwOVFmUHpGHIElKJLzO5Nj+lHzo==_-1030582931&query=%E9%98%BF%E9%87%8C%E5%B7%B4%E5%B7%B4&'
res = requests.get(url, headers=headers, timeout=10).text
# print(res)
p_href='<a href="(.*?)" id="uigs_.*?" target="_blank">'
href = re.findall(p_href, res, re.S)
print(href)