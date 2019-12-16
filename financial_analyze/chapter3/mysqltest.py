# -- coding: utf-8 --
import pymysql
conn = pymysql.connect(host="127.0.0.1", user="root", password="root", database="test", charset="utf8")
cur = conn.cursor()
sql = 'insert into baidunews (company,title,href,date,source) values (%s,%s,%s,%s,%s)'
cur.execute(sql, (1,1,1,1,1))
conn.commit()
cur.close()
conn.close()