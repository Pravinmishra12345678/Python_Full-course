import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 q='select * from assignment'
 cmd.execute(q)
 rows=cmd.fetchall()
 for row in rows:
     print(row)

 db.close()
except pymysql.InternalError as e:
    print("Error :",e)