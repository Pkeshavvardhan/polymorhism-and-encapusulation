class computer:
    def __init__(self):
        self.__maxprice=200
    def sell(self):
        print(f"selling price={self.__maxprice}")
    def setmaxprice(self, price):
        self.__maxprice=price

ob1=computer()
ob1.sell()

ob1.__maxprice=2000
ob1.sell()

ob1.setmaxprice(2000)
ob1.sell()