from bill import Bill
from bill import BillMethods
from bill_type import BillType
from apartament import Apartament
from apartament import Apartaments

apartaments = Apartaments()

def addBill(apartamentNumber,billType,cost):
    bill = Bill(billType,cost)
    apartaments.get(apartamentNumber).addBill(bill)




    
