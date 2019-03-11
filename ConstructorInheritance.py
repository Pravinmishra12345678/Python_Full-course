class base:
    def __init__(self):
        self.__x=input('Enter Value X:')
    def showx(self):
        print('Base Version',self.__x)
class derive(base):
    def __init__(self):
        super(derive,self).__init__() # inheriting constructor
        self.__y=input('Enter Value Y:')
    def showy(self):
        print('Derive Version', self.__y)

D=derive()
D.showx()
D.showy()



