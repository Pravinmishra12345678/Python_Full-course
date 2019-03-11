import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 rollno=input('roll no:')
 name=input('Name:')
 e=int(input('e'))
 h=int(input('h'))
 p=int(input('p'))
 m =int(input('m'))
 totalmarks = e+h+p+m
 percentage = (e+h+p+m)/4
 division = 0
 i = True
 while i :
  if percentage>60 :
      division = 1
      i = False
  elif percentage> 40:
     division = 2
  else :
      division = 3
 q="insert into m values({0},'{1}',{2},{3},'{4}',{5},{6},{7},'{8}')".format(rollno,name,e,h,p,m,totalmarks,percentage,division)
 cmd.execute(q)
 db.commit()
 print('Record Submitted....')
 db.close()
except pymysql.InternalError as e:
    print("Error :",e)