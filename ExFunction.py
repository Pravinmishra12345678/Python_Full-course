def fact(n):
    f=1
    for i in range(n,1,-1):
        f=f*i
    return f
x=float(input('Enter X:'))
n=int(input('Enter N:'))
sum=1
for i in range(3,n,2):
    sum=sum+((x**i)/fact(i))

print(sum)