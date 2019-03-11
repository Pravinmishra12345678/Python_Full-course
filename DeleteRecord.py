import pymysql
try:
 db=pymysql.connect(host='localhost',user='root',password='123',db='db')
 cmd=db.cursor()
 id=input('Enter rollnumber u want to delete data of:')
 q='select * from v where rollno={0}'.format(id)
 cmd.execute(q)
 row=cmd.fetchone()
 if(row==None):
     print('Record Not Found..')
     
 else:
    #print(row)
    print('rollno:',row[0])
    print('name:', row[1])
    print('e:', row[2])
    print('h:', row[3])
    print('p:', row[4])
    print('m:', row[5])
    print('totalmarks:', row[6])
    print('percentage:', row[7])
    ch=input('Are U Sure Y/N')
    if(ch=='y' or ch=='Y'):
        q='delete from v where rollno={0}'.format(id)
        cmd.execute(q)
        print('Record Deleted...')
        db.commit()
 db.close()
except pymysql.InternalError as e:
    print("Error :",e)