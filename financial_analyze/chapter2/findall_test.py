# -- coding: utf-8 --

import  re

content='assd 123 asdsdf'
result=re.findall('\d\d\d',content)
print(result)

test1='aaaAhadoopMMMMM'
result1 = re.findall('aaaA(.*?)MMMM', test1)
print(result1)
#  (.*?)非贪婪匹配  .*?


