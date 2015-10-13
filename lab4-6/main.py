from bill import Bill
from bill_type import BillType

def createBill(type,cost):
    return Bill(type,cost)

def readBill():
    type = int(input("What is the bill type? 1 = Water, 2 = Sewerage, 3 = Gas, 4 = Other "))
    cost = int(input("What is the bill cost ? "))
    return createBill(type,cost)




    
