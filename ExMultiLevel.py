class Employee:
    def GetEmployee(self):
        self.__id=input('Enter Employee Id:')
        self.__name=input('Enter Employee Name:')
        self.__salary =int(input('Enter Employee Salary:'))
    def PutEmployee(self):
        print(self.__id,self.__name,self.__salary)
    def GetSalary(self):
         return self.__salary

class Perks(Employee):
    def GetPerks(self):
         self.GetEmployee()
         self.__da =int(input('Enter DA:'))
         self.__hra =int(input('Enter Hra:'))
         self.__ta = int(input('Enter TA:'))
    def PutPerks(self):
         self.PutEmployee()
         print(self.__da,self.__hra,self.__ta)
    def TotalPerks(self):
        return (self.__da+self.__hra+self.__ta)

class NetSalary(Perks):
    def GetNetSalary(self):
        self.GetPerks()
        self.__netsalary=self.GetSalary()+self.TotalPerks()
    def PutNetSalary(self):
         self.PutPerks()
         print(self.__netsalary)

E=NetSalary()
E.GetNetSalary()
E.PutNetSalary()