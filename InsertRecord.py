import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 rollno=input('roll no:')
 name=input('Name:')
 e=input('e')
 h=input('h')
 p=input('p')
 m =input('m')
 q="insert into assignment values({0},'{1}',{2},{3},'{4}',{5})".format(rollno,name,e,h,p,m)
 cmd.execute(q)
 db.commit()
 print('Record Submitted....')
 db.close()
except pymysql.InternalError as e:
    print("Error :",e)