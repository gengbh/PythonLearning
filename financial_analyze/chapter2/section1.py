# -- coding: utf-8 --
import requests
# url='https://www.baidu.com/s?wd=%E7%BF%BB%E8%AF%91&rsv_spt=1&rsv_iqid=0xaf08ba1a00149796&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=%25E7%25BF%25BB%25E8%25AF%2591&rsv_t=1b1fwfQ48foIHiBHLd6PKt85i3dOCYLW%2FwPrLrHBPfCg5I%2BWMCzVYhHi2NmRZlkRxQfz&rsv_pq=f38ceb5b00176309&rsv_sug3=29&rsv_sug1=26&rsv_sug7=100&rsv_sug2=0&inputT=6&rsv_sug4=135254&rsv_sug=1'
# url='https://www.baidu.com/s?wd=%E7%BF%BB%E8%AF%91&rsv_spt=1&rsv_iqid=0xaf08ba1a00149796&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=%25E7%25BF%25BB%25E8%25AF%2591&rsv_t=1b1fwfQ48foIHiBHLd6PKt85i3dOCYLW%2FwPrLrHBPfCg5I%2BWMCzVYhHi2NmRZlkRxQfz&rsv_pq=f38ceb5b00176309&rsv_sug3=29&rsv_sug1=26&rsv_sug7=100&rsv_sug2=0&inputT=6&rsv_sug4=135254&rsv_sug=1'
# url1='''https://www.baidu.com/s?wd=hadoop&rsv_spt=1&rsv_iqid=0xbeebb3160019f788&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&prefixsug=hadoop&rsp=1&inputT=2809&rsv_sug4=3937&rsv_sug=1'''
url2='https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&tn=news&word=%E7%89%B9%E6%96%AF%E6%8B%89&rsv_sug3=2&rsv_sug4=185&rsv_sug1=2&oq=te&rsv_sug2=0&f=3&rsp=0&rsv_dl=news_t_sug&inputT=2281'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
res=requests.get(url2,headers=header).text
print(res)