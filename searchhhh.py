import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 id=input('Enter Product Id U Want To Search:')
 q='select * from b where productid={0}'.format(id)
 cmd.execute(q)
 row=cmd.fetchone()
 if(row==None):
     print('Record Not Found..')
 else:
    #print(row)
    print('Product Id:',row[0])
    print('Product Name:', row[1])
    print('Product Rate:', row[2])
    print('Product Stock:', row[3])
    print('Picture:', row[4])

 db.close()
except pymysql.InternalError as e:
    print("Error :",e)