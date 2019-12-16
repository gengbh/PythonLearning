# -- coding: utf-8 --
#使用panda库对excel进行一些简单的操作


import  pandas

df = pandas.read_excel("excel_operator_demo.xlsx")
print(df.columns)

head = df.head(8)
print(head)


print("-------------------------------------------------------------------")
ix = df.ix[[1, 2]]
print("需要打印的值：\n{0}".format(ix))

print("-------------------------------------------------------------------")
test_data=[]
for i in df.index.values:
    data = df.ix[i, ['id', 'name', 'score', 'sex']].to_dict()
    test_data.append(data)

print(test_data)
