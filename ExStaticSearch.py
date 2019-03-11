class Student:
    def GetStudent(self):
        self.__rollno=input("Enter Roll No:")
        self.__name=input("Enter Name:")
        self.__p=int(input('Enter Physics Marks:'))
        self.__c = int(input('Enter Chemistry Marks:'))
        self.__m = int(input('Enter Maths Marks:'))
    def ShowResult(self):
        print("ROll No:",self.__rollno)
        print ("Name:",self.__name)
        print("Physics:",self.__p)
        print("Chemistry:", self.__c)
        print("Maths:", self.__m)
        total=self.__p+self.__c+self.__m
        print ('Total:',total)
        per=total/3
        print('Percentage:',per)
    @staticmethod
    def Search(SL,min,max):
      R=list()
      for S in SL:
        per=(S.__p+S.__c+S.__m)/3
        if(per>=min and per<=max):
            R.append(S)
      return R



SL=list() # or SL=[]
ch=True
while ch:
    S=Student()
    S.GetStudent()
    SL.append(S)
    ch=input("Do U Want To Add More Students (Y/N)?")
    if(ch=='n' or ch=='N'):
        ch=False

min=float(input('Enter Min Percentage?'))
max=float(input('Enter Max Percentage?'))

R=Student.Search(SL,min,max)
for S in R:
    S.ShowResult()


