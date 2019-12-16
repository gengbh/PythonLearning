# -- coding: utf-8 --
#将代码抽取成方法
import  requests
import re
import time
import pymysql
headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
conn = pymysql.connect(host="127.0.0.1", user="root", password="root", database="test", charset="utf8")
def baidu(company,page):
    num=(page-1)*10
    url = 'https://www.baidu.com/s?rtt=4&bsst=1&cl=2&tn=news&word='+company+'&pn'+str(num)
    res = requests.get(url, headers=headers,timeout=10).text
    # 提取出新闻来源和日期
    p_info = '<p class="c-author">(.*?)</p>'
    info = re.findall(p_info, res, re.S)
    # 提取新闻的网址和标题
    p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
    href = re.findall(p_href, res, re.S)
    # 提取标题
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    title = re.findall(p_title, res, re.S)

    # 清晰时间和来源
    source = []
    date = []
    for i in range(len(info)):
        # info[i]=info[i].strip()
        info[i] = re.sub('<.*?>', '', info[i])
        source.append(info[i].split('&nbsp;&nbsp;')[0])
        date.append(info[i].split('&nbsp;&nbsp;')[1])
        source[i] = source[i].strip()
        #日期格式处理
        date[i] = date[i].strip()
        date[i]=date[i].split(' ')[0]
        date[i]=re.sub('年','-',date[i])
        date[i] = re.sub('月', '-', date[i])
        date[i] = re.sub('日', '', date[i])
        if ('小时' in date[i] or '分钟' in date[i]):
            date[i]=time.strftime('%Y-%m-%d')
        else:date[i]=date[i]
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        # print(date[i])
        #评分
        score=[]
        keywords=['违约','诉讼','兑付','阿里','百度','京东','互联网']
    for i in range(len(title)):
        num1=0
        try:
            article=requests.get(href[i],headers=headers,timeout=10).text
        except:
            article='爬取失败'
        try:
            article=article.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')
            except:
                article=article
        p_article='<p>(.*?)</p>'
        article_main=re.findall(p_article,article)
        article=''.join(article_main)
        print(article)
        for k in keywords:
            if (k in keywords) or (k in title[i]):
                num1-=5
        score.append(num1)
        # company_re=company[0]+ '.{0,5}' +company[-1]
        # if len(re.findall(company_re),article) < 1
        # if company not in title[i]:
        company_re = company[0] + '.{0,5}' + company[-1]
        if len(re.findall(company_re, article)) < 1:
            title[i]=''
            href[i]=''
            date[i]=''
            source[i]=''
            score[i]=''
    while '' in title:
        title.remove('')
    while '' in href:
        href.remove('')
    while '' in date:
        date.remove('')
    while '' in source:
        source.remove('')
    while '' in score:
        score.remove('')
        #打印数据
    for i in  range(len(title)):
            print(str(i+1) + '. ' + title[i] + '(' + date[i] + '-' + source[i] + ')')
            print(href[i])
            print(company+'评分为'+str(score[i]))
    #简单过滤标题
    # for i in range(len(title)):
    #     if company not  in title[i]:
    #         title[i]=''
    #         href[i]=''
    #         date[i]=''
    #         source[i]=''
    # while '' in title:
    #     title.remove('')
    # while '' in href:
    #     href.remove('')
    # while '' in date:
    #     date.remove('')
    # while '' in source:
    #     source.remove('')
    # print(str(i + 1) + '. ' + title[i] + '(' + date[i] + '-' + source[i] + ')')
    # print(href[i])
    #将爬取的数据写入到文件中
    # file1=open('D:\\百度爬虫.txt','a')
    # file1.write(company+'数据爬取完成！' +'\n' +'\n')
    # for j in range(len(title)):
    #     file1.write(str(j+1)+'. '+title[j]+'('+date[j]+'-'+source[j]+')'+'\n')
    #     file1.write(href[j]+'\n')
    # file1.write('----------------------------------------'+'\n'+'\n')
    # file1.close()
    #将爬取到的数据存入到mysql中
    for i in range(len(title)):
        #数据去重
        cur = conn.cursor()
        sql1='select title from baidunews where company = %s'
        cur.execute(sql1,company)
        data_all=cur.fetchall()
        # print('所有标题'+str(data_all))
        title_all=[]
        for j in range(len(data_all)):
            title_all.append(data_all[j])
            # print('数据库去重标题'+str(data_all[j]))
        if title[i] not in title_all:
            sql='insert into baidunews (company,title,href,date,source，score) values (%s,%s,%s,%s,%s)'
            cur.execute(sql,(company,title[i],href[i],date[i],source[i]),score[i])
            conn.commit()
        cur.close()



company=['华能信托','阿里巴巴','百度集团','腾讯','京东']
for i in company:
    for j in range(20):
        # try:
            baidu(i,j+1)
        #     print(i+'第'+str(j+1)+'页爬取成功！')
        # except:
        #     print(i + '第' + str(j + 1) + '页爬取不成功！')
conn.close()
# time.sleep(10800)
