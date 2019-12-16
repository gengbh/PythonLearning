# -- coding: utf-8 --
#5.4.3从数据库获取每日评分
import  pymysql
import time
#pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test', charset='utf8')
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test', charset='utf8')
company='阿里巴巴'
today=time.strftime('%Y-%m-%d')
cur=conn.cursor()
sql='select * from test.baidunews where company=%s and date=%s'
cur.execute(sql,(company,today))
data = cur.fetchall()

for i in range(len(data)):
    print(data[i])

score=100
for i in range(len(data)):
    score+=int(data[i][6])
conn.commit()
cur.close()
conn.close()

print('舆情得分:'+str(score))
