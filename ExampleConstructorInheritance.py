class Media:
    def __init__(self,title,price):
        self.__title=title
        self.__price=price
    def ShowMedia(self):
        print(self.__title,self.__price)
class Magzine(Media):
      def __init__(self,title,price,pages):
          super(Magzine,self).__init__(title,price)
          self.__pages=pages
      def ShowMagzine(self):
          self.ShowMedia()
          print(self.__pages)

M1=Magzine('India Today',15,105)
M1.ShowMagzine()


