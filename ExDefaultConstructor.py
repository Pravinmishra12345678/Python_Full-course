class Person:
    def __init__(self):
        self.__name=input('Enter Name:')
        self.__age=int(input('Enter Age:'))
    def ShowPerson(self):
        print(self.__name,self.__age)
PL=list()
ch=True
while ch:
   P=Person()
   PL.append(P)
   ch=input("Continue Y/N?")
   if(ch=='N' or ch=='n'):
       ch=False

for P in PL:
    P.ShowPerson()
