class Person:
    def __init__(self,id,name,age):
        self.__id=id
        self.__name=name
        self.__age=age
    def ShowPerson(self):
        print(self.__id,self.__name,self.__age)


PD = dict()
ch = True
while ch:
    id=input("Enter Id:")
    name = input("Enter Name:")
    age=int(input("Enter Age:"))

    P = Person(id,name,age)
    PD.setdefault(id,P)
    ch = input("Continue Y/N?")
    if (ch == 'N' or ch == 'n'):
        ch = False

for P in PD.values():
    P.ShowPerson()


