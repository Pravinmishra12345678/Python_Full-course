class Student:
    def GetStudent(self):
        self.__rollno=input("Enter Roll No:")
        self.__name=input("Enter Name:")
        self.__p=int(input('Enter Physics Marks:'))
        self.__c = int(input('Enter Chemistry Marks:'))
        self.__m = int(input('Enter Maths Marks:'))
    def Result(self):
        total=self.__p+self.__c+self.__m
        per=total/3
        if(per>45):
            return 'PASS'
        else:
            return 'FAIL'




SL=list() # or SL=[]
ch=True
while ch:
    S=Student()
    S.GetStudent()
    SL.append(S)
    ch=input("Do U Want To Add More Students (Y/N)?")
    if(ch=='n' or ch=='N'):
        ch=False

RS=list(map(lambda X:X.Result(),SL))
print(RS)


























