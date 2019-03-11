mydata='Varable of MyLib'
def fact(n):
    f=1
    while(n>1):
        f=f*n
        n=n-1
    return f

def sqr(n):
    return (n*n)

def table(n):
     i=1
     while(i<=10):
         t=n*i
         print(n,'x',i,'=',t)
         i=i+1