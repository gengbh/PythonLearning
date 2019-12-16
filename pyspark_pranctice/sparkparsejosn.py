# -- coding: utf-8 --
import os
os.chdir(r"D:\py_data\person\PythonLearning\reptile")
os.environ['PYSPARK_PYTHON']='D:\Anaconda3\envs\python_learning\python.exe'
from pyspark import SparkContext
logFile = "citycode.json"
sc = SparkContext("local","Simple App")
data=sc.textFile(logFile).map(lambda  x:(x.split(","))).collect()
print(data)