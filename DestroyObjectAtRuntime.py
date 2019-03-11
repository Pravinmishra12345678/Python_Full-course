class Person:
    def __init__(self,id,name,age):
        self.__id=id
        self.__name=name
        self.__age=age
    def ShowPerson(self):
        print(self.__id,self.__name,self.__age)
    def __del__(self):
        print('Person Destroyed ',self.__name,self.__age)

P1=Person(100,'James',22)
P1.ShowPerson()
P1=Person(100,'Smith',45)
P1.ShowPerson()
print('Press Any Key to Cont...')
input()
print('END OF PROGRAM')




