# -- coding: utf-8 --
import numpy as np
a=[1,2,3,4]
b=np.array([1,2,3,4])
print(a)
print(type(a))
print(b)
print(type(b))
print(a[1])
print(b[1])
print(a[0:2])
print(b[0:2])
#做运算
c=a*2
d=b*3
print(c)
print(d)
print('-----------------------------------------')
e=[[1,2],[3,4],[5,6]]
f=np.array([[1,2],[3,4],[5,6]])
print(e)
print('------------------------------------')
print(f)
print('------------------------------------')
#创建一维数组
g=np.array([1,2,3,4])
#创建二维数组
h=np.array([[1,2],[3,4],[5,6]])

#创建数组其他方式
x=np.arange(5)
print(x)
y=np.arange(5,10)
print(y)
z=np.arange(0,20,4)
print(z)