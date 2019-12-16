# -- coding: utf-8 --
#pandas基础
import  pandas as pd
s1=pd.Series(['一','二','三'])
print(s1)
print('------------------------------------------------------')
#datafream 的创建
a = pd.DataFrame([[1, 2], [3, 4], [5, 6]])
b = pd.DataFrame([[1, 2], [3, 4], [5, 6]],columns=['date','score'],index=['A','B','C'])
print(a)
print('---------------------------')
print(b)
print('---------------------------')
#创建datafream的几种方式
c = pd.DataFrame()
date=[1,3,5]
score=[2,4,6]
c['date']=date
c['score']=score
print(c)
#通过字典创建
d = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=['one', 'two', 'three'])
print(d)
#orient
e = pd.DataFrame.from_dict({'a': [1, 2, 3], 'b': [4, 5, 6]}, orient='index')
print(e)