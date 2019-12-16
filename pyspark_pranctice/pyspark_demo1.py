# -- coding: utf-8 --
import os
os.chdir("D:\py_data\person\PythonLearning\pyspark_pranctice")
os.environ['PYSPARK_PYTHON']='D:\Anaconda3\envs\python_learning\python.exe'
from pyspark import SparkContext
logFile = "pytest.txt"
sc = SparkContext("local","Simple App")
data=sc.textFile(logFile).map(lambda x: (x.split(" ")))
data.foreach(lambda x:(print(int(x[2])/2)))

print("--------------------------------------------------------")
# key = data.reduceByKey(lambda x, y: (int(x) + int(y)))
# key.foreach(lambda x:(print(x)))

