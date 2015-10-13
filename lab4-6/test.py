import main
from bill import Bill
from bill_type import BillType

def testCreateBill():
    bill = createBill(BillType.Water,100)
    assert(bill.type == BillType.Water and bill.cost == 100)

testCreateBill()
