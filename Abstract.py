from abc import ABC,abstractmethod
class Student(ABC):
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def put(self):
        pass

class BA(Student):
    def get(self):
      self.__rollno=input("Enter Roll No:")
      self.__name=input("Enter Name:")
      self.__his=input("History Marks:")
      self.__eco = input("Econmomics Marks:")
    def put(self):
        print(self.__rollno,self.__name,self.__his,self.__eco)

class BSc(Student):
    def get(self):
      self.__rollno=input("Enter Roll No:")
      self.__name=input("Enter Name:")
      self.__phy=input("Physics Marks:")
      self.__chem = input("Chemistry Marks:")
    def put(self):
        print(self.__rollno,self.__name,self.__phy,self.__chem)

student=BA()
student.get()
student.put()

student = BSc()
student.get()
student.put()
