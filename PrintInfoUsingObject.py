class Person:
    def __init__(self,id,name,age):
        self.__id=id
        self.__name=name
        self.__age=age
    def __repr__(self):
        return "{0},{1},{2}".format(self.__id,self.__name,self.__age)

P=Person(100,'Peter',90)
print(P)

