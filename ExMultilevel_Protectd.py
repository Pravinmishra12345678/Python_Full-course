class Employee:
    def GetEmployee(self):
        self.__id=input('Enter Employee Id:')
        self.__name=input('Enter Employee Name:')
        self._salary =int(input('Enter Employee Salary:'))
    def PutEmployee(self):
        print(self.__id,self.__name,self._salary)

class Perks(Employee):
    def GetPerks(self):
         self.GetEmployee()
         self._da =int(input('Enter DA:'))
         self._hra =int(input('Enter Hra:'))
         self._ta = int(input('Enter TA:'))
    def PutPerks(self):
         self.PutEmployee()
         print(self._da,self._hra,self._ta)


class NetSalary(Perks):
    def GetNetSalary(self):
        self.GetPerks()
        self.__netsalary=self._salary+self._da+self._hra+self._ta
    def PutNetSalary(self):
         self.PutPerks()
         print(self.__netsalary)

E=NetSalary()
E.GetNetSalary()
E.PutNetSalary()