# -- coding: utf-8 --
# =============================================================================
# 5.4.2 完整版百度新闻数据挖掘系统 by 王宇韬
# =============================================================================

import requests
import re
import pymysql
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

def baidu(company,page):
    # 1.获取网页源代码（参考2.3、3.1、3.4节）
    num=page*10
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company+'&pn'+str(num)  # 其中设置rtt=4则为按时间排序，如果rtt=1则为按焦点排序
    res = requests.get(url, headers=headers, timeout=10).text

    # 2.编写正则提炼内容（参考3.1节）
    p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    p_info = '<p class="c-author">(.*?)</p>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    info = re.findall(p_info, res, re.S)

    # 3.数据清洗（参考3.1节）
    source = []  # 先创建两个空列表来储存等会分割后的来源和日期
    date = []
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])
        source.append(info[i].split('&nbsp;&nbsp;')[0])
        date.append(info[i].split('&nbsp;&nbsp;')[1])
        source[i] = source[i].strip()
        date[i] = date[i].strip()

        # 统一日期格式（参考5.1节）
        date[i] = date[i].split(' ')[0]
        date[i] = re.sub('年', '-', date[i])
        date[i] = re.sub('月', '-', date[i])
        date[i] = re.sub('日', '', date[i])
        if ('小时' in date[i]) or ('分钟' in date[i]):
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]

    # 4.舆情评分版本4及数据深度清洗（参考5.1和5.2和5.3节）
    score = []
    keywords = ['违约', '诉讼', '兑付', '阿里', '百度', '京东', '互联网']
    for i in range(len(title)):
        num = 0
        try:
            article = requests.get(href[i], headers=headers, timeout=10).text
        except:
            article = '爬取失败'

        try:
            article = article.encode('ISO-8859-1').decode('utf-8')
        except:
            try:
                article = article.encode('ISO-8859-1').decode('gbk')
            except:
                article = article
        p_article = '<p>(.*?)</p>'
        article_main = re.findall(p_article, article)  # 获取<p>标签里的正文信息
        article = ''.join(article_main)  # 将列表转换成为字符串
        for k in keywords:
            if (k in article) or (k in title[i]):
                num -= 5
        score.append(num)
        # 数据深度清洗（参考5.1节）
        company_re = company[0] + '.{0,5}' + company[-1]
        if len(re.findall(company_re, article)) < 1:
            title[i] = ''
            source[i] = ''
            href[i] = ''
            date[i] = ''
            score[i] = ''
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

    # 5.打印清洗后的数据（参考3.1节）
    for i in range(len(title)):
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + ' ' + source[i] + ')')
        print(href[i])
        print(company + '该条新闻的舆情评分为' + str(score[i]))

    # 6.将数据存入数据库及数据去重（参考4.4节和5.1节）
    for i in range(len(title)):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test', charset='utf8')
        cur = db.cursor()  # 获取会话指针，用来调用SQL语句

        # 6.1 查询数据，为之后的数据去重做准备
        sql_1 = 'SELECT * FROM baidunews WHERE company =%s'
        cur.execute(sql_1, company)
        data_all = cur.fetchall()
        title_all = []
        for j in range(len(data_all)):
            title_all.append(data_all[j][1])

        # 6.2 判断数据是否在原数据库中，不在的话才进行数据存储
        if title[i] not in title_all:
            sql_2 = 'INSERT INTO baidunews(company,title,href,source,date,score) VALUES (%s,%s,%s,%s,%s,%s)'  # 编写SQL语句
            cur.execute(sql_2, (company, title[i], href[i], source[i], date[i], score[i]))  # 执行SQL语句
            db.commit()  # 当改变表结构后，更新数据表的操作
        cur.close()  # 关闭会话指针
        db.close()  # 关闭数据库链接
    print('------------------------------------')  # 分割符


# 7.批量爬取多家公司（参考3.2节）
companys = ['华能信托', '阿里巴巴', '百度集团', '腾讯', '京东']
for company in companys:
    for page in range(20):
        try:
            baidu(company,page)
            print(company + '数据爬取并存入数据库成功')
        except:
            print(company + '数据爬取并存入数据库失败')
