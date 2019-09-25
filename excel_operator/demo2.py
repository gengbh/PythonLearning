# -- coding: utf-8 --

#练习xlrd
import xlrd
#打开excle读取数据
data=xlrd.open_workbook("excel_operator_demo.xlsx")
#打开一个工作表

# table= data.sheets()[0]  #索引获取

#table=data.sheet_by_index(0) #通过索引顺序获取

table=data.sheet_by_name("Sheet1")  #通过名称获取
nrows = table.nrows     #获取行数
ncols = table.ncols     #获取列数

row_values = table.row_values(2)
print(row_values)
print(ncols)
print(nrows)
print(table.cell(5,1))

# 返回所有Sheet对象名字的list
all_sheet = data.sheet_names()
print(all_sheet)

# 遍历返回的Sheet对象名字的list
for each_sheet_by_name in all_sheet:
    print("表名称为：{0}，类型为：{1}".format(each_sheet_by_name, type(each_sheet_by_name)))



