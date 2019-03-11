import pymysql
try:
 db=pymysql.connect(host='127.0.0.1',user='root',password='123',db='db',port=3306)
 cmd=db.cursor()
 q='create table m(rollno integer primary key,name varchar(25),e integer,h integer, p integer,m integer,totalmarks integer,percentage integer,division char)'
 cmd.execute(q)
 db.commit()
 print('Table Created')
 db.close()
except pymysql.InternalError as e:
    print("Error :",e)
