import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 id = input('enter the roll number u want to search for')
 q='select totalmarks,percentage,division from v where rollno={0}'.format(id)
 cmd.execute(q)
 rows=cmd.fetchall()
 for row in rows:
     print(row)

 db.close()
except pymysql.InternalError as e:
    print("Error :",e)