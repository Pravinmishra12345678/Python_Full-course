f=open('e:/mytext1.txt','wb')
for i in range(5):
   s=input('Enter Name:')
   f.write(bytes(s,'UTF-8'))
   f.write(bytes('\n','UTF-8'))
f.close()