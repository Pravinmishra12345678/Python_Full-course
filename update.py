import pymysql
try:
 db=pymysql.connect(host='127.0.0.1',user='root',password='123',db='db',port=3306)
 cmd=db.cursor()
 q='update v set p = 6 where rollno=1'
 cmd.execute(q)
 db.commit()
 print('Table Created')
 db.close()
except pymysql.InternalError as e:
    print("Error :",e)
