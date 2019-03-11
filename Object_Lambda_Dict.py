class Product:
    def GetProduct(self,code):
        self.__code=code
        self.__name = input('Enter Name:')
        self.__rate = int(input('Enter Rate:'))
    def ShowProduct(self):
        print(self.__code,self.__name,self.__rate)
    def GST(self):
        gst=self.__rate*18/100
        netamt=self.__rate+gst
        return [self.__rate,gst,netamt]
    def Price_gt_100(self):
         if(self.__rate>100):
             return True
         else:
             return False


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

#RS=list(map(lambda X:X.GST(),PL.values()))
#print(RS)
RS=list(filter(lambda X:X.Price_gt_100(),PL.values()))
for P in RS:
    P.ShowProduct()





