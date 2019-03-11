import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='morningbatch')
 cmd=db.cursor()
 min=input('Enter Min Rate:')
 max=input('Enter Max Rate:')
 q='select * from products where productrate between {0} and {1}'.format(min,max)
 cmd.execute(q)
 rows=cmd.fetchall()
 for row in rows:
     print(row)
except:
    print('Error')
