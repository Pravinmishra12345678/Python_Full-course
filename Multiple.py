class ProductionUnitOne:
    def GetProductionUnitOne(self):
        self._totalOne=int(input("Enter Total Production Unit One:"))

    def PutProductionUnitOne(self):
         print("Unit One:",self._totalOne)


class ProductionUnitTwo:
    def GetProductionUnitTwo(self):
        self._totalTwo = int(input("Enter Total Production Unit Two:"))

    def PutProductionUnitTwo(self):
        print("Unit Two:", self._totalTwo)


class TotalProduction(ProductionUnitOne,ProductionUnitTwo):
    def GetTotalProduction(self):
        self.GetProductionUnitOne()
        self.GetProductionUnitTwo()
        self.__total=self._totalOne+self._totalTwo
    def PutTotalProduction(self):
        self.PutProductionUnitOne()
        self.PutProductionUnitTwo()
        print('Total Production:',self.__total)

P=TotalProduction()
P.GetTotalProduction()
P.PutTotalProduction()













