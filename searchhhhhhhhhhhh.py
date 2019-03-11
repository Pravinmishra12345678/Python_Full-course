import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 frompercentage = int(input('Enter minimum percentage'))
 topercentage = int(input('Enter maximum percentage'))
 q='select percentage from v where percentage between {} and {}'.format(frompercentage,topercentage)
 cmd.execute(q)
 row=cmd.fetchone()
 for i in row:
     print(i)
except :
    print('Error')