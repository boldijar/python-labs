    from bill_type import BillType

class Bill:

    def __init__(self, type, cost):
        self.type = type
        self.cost = cost
        
      
class BillMethods:

    @staticmethod
    def createBill(type,cost):
        return Bill(type,cost)
    
    @staticmethod
    def readBill():
        type = int(input("What is the bill type? 1 = Water, 2 = Sewerage, 3 = Gas, 4 = Other ) : "))
        cost = int(input("What is the bill cost ? "))
        return BillMethods.createBill(type,cost)
