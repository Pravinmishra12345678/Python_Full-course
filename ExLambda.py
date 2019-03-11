def fact(n):
    f=1
    while(n>1):
        f=f*n
        n=n-1
    return f

k=lambda n:list((fact(i) for i in range(1,n)))
m=lambda n:(fact(i) for i in range(1,n))

z=lambda:(fact(i) for i in (5,2,8,4))
li=[5,2,8,5]
s=lambda:(fact(i) for i in li)

j=k(5)
print(j)

p=m(5)
print(list(p))

r=z()
print(list(r))
