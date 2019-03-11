import pymysql
db=pymysql.connect(host='127.0.0.1',user='root',password='123',db='db')
cmd=db.cursor()
roll=123
marks=123
q="insert into pravin values({0},{1})".format(roll,marks)
cmd.execute(q)
db.commit()
db.close()

