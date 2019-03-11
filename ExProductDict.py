class Product:
    def GetProduct(self,code):
        self.__code=code
        self.__name = input('Enter Name:')
        self.__rate = int(input('Enter Rate:'))
    def ShowProduct(self):
        print(self.__code,self.__name,self.__rate)


    def Sale(self):
        qty=int(input("Enter Quantity:"))
        amt=self.__rate*qty
        print('Total Amount:',amt)


PL=dict() # or SL=[]
ch=True
while ch:
    P=Product()
    code=input('Enter Product Id:')
    P.GetProduct(code)
    PL.setdefault(code,P)
    ch=input("Do U Want To Add More Product (Y/N)?")
    if(ch=='n' or ch=='N'):
        ch=False
code=input('Enter Product Code U want to Search:')
P=PL.get(code,'Record Not Found')
if(isinstance(P,Product)):
 P.ShowProduct()
 P.Sale()
else:
  print(P)

PList=PL.values();
for P in PList:
    P.ShowProduct()
















