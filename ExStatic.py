class PNB:
    bankbalance=0
    def OpenAccount(self):
        self.__accno=input("Enter Account Number:")
        self.__name = input("Enter Account Name:")
        self.__balance= int(input("Enter Account Balance:"))
        PNB.bankbalance=PNB.bankbalance+self.__balance
    def ShowAccount(self):
        print(self.__accno,self.__name,self.__balance)
    @staticmethod
    def ShowBankBalance():
        print(PNB.bankbalance)
    @classmethod
    def ShowPNBBalance(cls):
        print(cls.bankbalance)
CL=list()
for i in range(3):
    C=PNB()
    C.OpenAccount()
    CL.append(C)

for C in CL:
    C.ShowAccount()

PNB.ShowBankBalance()
PNB.ShowPNBBalance()

