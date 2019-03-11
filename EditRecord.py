import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='morningbatch')
 cmd=db.cursor()
 id=input('Enter Product Id U Want To Edit:')
 q='select * from products where productid={0}'.format(id)
 cmd.execute(q)
 row=cmd.fetchone()
 if(row==None):
     print('Record Not Found..')
 else:
    #print(row)
    print('Product Id:',row[0])
    print('1]Product Name:', row[1])
    print('2]Product Rate:', row[2])
    print('3]Product Stock:', row[3])
    print('4]Picture:', row[4])
    print('5]Exit')
    f=input('Which Field U Want to Edit?')
    pat=None
    if(f=='1'):
        npn=input('Enter New Product Name:')
        pat="productname='{0}'".format(npn)
    elif(f=='2'):
        npr = input('Enter New Product Rate:')
        pat = "productrate={0}".format(npr)
    elif(f=='3'):
        nps = input('Enter New Product Stock:')
        pat = "productstock={0}".format(nps)
    elif(f=='4'):
        npi = input('Enter New Product Image:')
        pat = "productimage='{0}'".format(npi)

    if(pat!=None):
         q='update products set {0} where productid={1}'.format(pat,id)
         cmd.execute(q)
         print('Record Updated')
         db.commit()

 db.close()
except pymysql.InternalError as e:
    print("Error :",e)

