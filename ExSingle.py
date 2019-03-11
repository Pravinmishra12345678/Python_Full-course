class Employee:
    def GetEmployee(self):
        self.__id=input('Enter Employee Id:')
        self.__name=input('Enter Employee Name:')
        self.__salary = input('Enter Employee Salary:')
    def PutEmployee(self):
        print(self.__id,self.__name,self.__salary)
class Perks(Employee):
    def GetPerks(self):
         self.GetEmployee()
         self.__da = input('Enter DA:')
         self.__hra = input('Enter Hra:')
         self.__ta = input('Enter TA:')
    def PutPerks(self):
         self.PutEmployee()
         print(self.__da,self.__hra,self.__ta)
E=Perks()
#Derive Class Constructor always invoke the
#base class Default Constructor Implicitly
#E.GetEmployee()
E.GetPerks()

#E.PutEmployee()
E.PutPerks()


