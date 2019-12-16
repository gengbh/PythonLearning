# -- coding: utf-8 --
#查看股票信息 tushare库的使用
import  tushare as ts
df=ts.get_hist_data('000002',start='2018-01-01',end='2019-09-30')
print(df)