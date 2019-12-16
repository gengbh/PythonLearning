# -- coding: utf-8 --
import  pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="root", database="test", charset="utf8")
cursor = conn.cursor()
sql="select * from test;"
sql1="insert into test (id,section,score,nid) values (%s,%s,%s,%s)"
# cursor.execute(sql1,[9,'220-230',65,5])
cursor.execute(sql)
# conn.commit()
cursor.execute(sql)
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()