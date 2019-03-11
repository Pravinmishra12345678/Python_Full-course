class Employee:
    def GetEmployee(self):
        self.__id=input('Enter Employee Id:')
        self.__name=input('Enter Employee Name:')
        self.__salary = input('Enter Employee Salary:')
    def PutEmployee(self):
        print(self.__id,self.__name,self.__salary)

class Faculty(Employee):
    def GetFaculty(self):
        self.GetEmployee()
        self.__subject = input('Enter Employee Subject:')

    def PutFaculty(self):
        self.PutEmployee()
        print(self.__subject)


class Admin(Employee):
    def GetAdmin(self):
        self.GetEmployee()
        self.__work = input('Enter Employee Work:')

    def PutAdmin(self):
        self.PutEmployee()
        print(self.__work)

E1=Faculty()
E2=Admin()
E1.GetFaculty()
E1.PutFaculty()
E2.GetAdmin()
E2.PutAdmin()