class Product:
    def GetProduct(self):
        self.__code=input('Enter Code:')
        self.__name = input('Enter Name:')
        self.__rate = int(input('Enter Rate:'))
    def ShowProduct(self):
        print(self.__code,self.__name,self.__rate)
    def Search(self,code):
        if(code==self.__code):
            return  True
        else:
            return  False

    def Sale(self):
        qty=int(input("Enter Quantity:"))
        amt=self.__rate*qty
        print('Total Amount:',amt)


PL=list() # or SL=[]
ch=True
while ch:
    P=Product()
    P.GetProduct()
    PL.append(P)
    ch=input("Do U Want To Add More Product (Y/N)?")
    if(ch=='n' or ch=='N'):
        ch=False
code=input('Enter Product Code U want to Search:')
found=False
for P in PL:
    found=P.Search(code)
    if(found):
        P.ShowProduct()
        P.Sale()
        break;

if(not found):
    print('Record Not Found....')



