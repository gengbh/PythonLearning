# -- coding: utf-8 --
import  numpy as np
from scipy.optimize import fsolve
"""numpy数组的简单练习"""
np_array = np.array([2,1,3,4,6,4]) #创建数组
print(np_array)
print(np_array[:3]) #输出数组的前三个数字
print(np_array.min()) #输出数组的最小值

b = np.array([[1, 2, 3], [23, 43, 56]]) #创建二维数组
print(b)

'''求解非线性方程 2x1+x2^2=1  x1^2-2x=2'''
def f(x):
    x1=x[0]
    x2=x[1]
    return [2*x1 - x2**2 -1,x1**2 - x2 -2]


result = fsolve(f, [1,1])
print(result)

from scipy import integrate  #导入积分函数
def g(x):
    return (16-x**2)**0.5
pi_2,err=integrate.quad(g,0,3)
print(pi_2)


import matplotlib.pyplot as plt  #导入matplotlib

x = np.linspace(0, 10, 1000) #设置自变量x
y=np.sin(x) + 1   #设置因变量y
z=np.cos(x**2)+1  #设置因变量z

plt.figure(figsize=(8,4))  #设置图像大小
plt.plot(x,y,label='$\sin x+1$' ,color = 'red',linewidth = 2)  #作图 设置标签 线条颜色 线条大小
plt.plot(x,z,'b--',label='$\cos x^2+1$' ,color= 'blue',linewidth= 2)  #作图 设置标签 线条颜色 线条大小
plt.xlabel('Times(s) ')  # x轴名称
plt.xlabel('Volt ')  # y轴名称
plt.title('example')  #设置标题名称
plt.ylim(0,2.2)  #设置y轴范围
plt.legend()   #显示图例
plt.show()


from statsmodels.tsa.stattools import adfuller as ADF

adf = ADF(np.random.rand(100))
print(adf)