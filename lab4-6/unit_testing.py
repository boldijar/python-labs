import unittest
from apartament_controller import ApartamentController
from validator import IntValidator
from bill_type import BillType
class TestController(unittest.TestCase):

    def testAddBill(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        self.assertEqual(apartamentController.all[0].bills[0].cost,100)

        
    def testGetBillName(self):
        apartamentController = ApartamentController()
        self.assertEqual(apartamentController.getBillTypeName(BillType.Water),"Water")


    
    def testEditBill(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.editBill(0,0,50,BillType.Water)
        self.assertEqual(apartamentController.all[0].bills[0].cost,50)

    
    def testAllApartamentAndBills(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        self.assertEqual(apartamentController.getAllApartamentsAndBills(),
                         "Apartament #0 , Bill id: 0 , type: Water , cost: 100\n")



    def testGetApartamentCost(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Water,5)
        self.assertEqual(apartamentController.getApartamentCost(0),105)

    
    def testGetApartamentsWithCostGreatherThan(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(1,BillType.Water,51)
        apartamentController.addBill(1,BillType.Water,51)
        self.assertEqual(len(apartamentController.getApartamentsWithCostGreatherThan(100)),1)


    
    def testGetApartamentsCount(self):
        apartamentController = ApartamentController()
        self.assertEqual(apartamentController.getApartamentsCount(),100)

            
    def testGetCertainBillsFromAllApartaments(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(1,BillType.Gas,100)
        apartamentController.addBill(2,BillType.Gas,100)
        self.assertEqual(len(apartamentController.getCertainBillsFromAllApartaments(BillType.Gas)),2)


    def testGetBillsCost(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Water,150)
        apartamentController.addBill(0,BillType.Water,150)
        self.assertEqual(apartamentController.getBillsCost(apartamentController.all[0].bills),400)

 
    def testClearApartamentBills(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Water,150)
        apartamentController.addBill(0,BillType.Water,150)
        apartamentController.clearApartamentBills(0)
        self.assertEqual(len(apartamentController.all[0].bills),0)

 
    def testClearApartamentCertainBills(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Gas,100)
        apartamentController.addBill(0,BillType.Gas,100)
        apartamentController.clearApartamentCertainBills(0,BillType.Gas)
        self.assertEqual(len(apartamentController.all[0].bills),1)


    def testClearCertainBillsFromAllApartaments(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Gas,100)
        apartamentController.addBill(0,BillType.Gas,100)
        apartamentController.addBill(1,BillType.Water,100)
        apartamentController.addBill(1,BillType.Gas,100)
        apartamentController.addBill(1,BillType.Gas,100)
        apartamentController.clearCertainBillsFromAllApartaments(BillType.Gas)
        self.assertEqual(len(apartamentController.all[0].bills),1)
        self.assertEqual(len(apartamentController.all[1].bills),1)


 

    def testIntValidator(self):
        self.assertEqual(IntValidator.valid("123",0,200),True)
        self.assertEqual(IntValidator.valid("lala",0,200),False)
        self.assertEqual(IntValidator.valid("123",0,50),False)

    def testDeleteAllBillsFromApartamentsInRanget(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Water,5)
        apartamentController.addBill(1,BillType.Water,100)
        apartamentController.addBill(1,BillType.Water,5)
        apartamentController.addBill(2,BillType.Water,100)
        apartamentController.addBill(2,BillType.Water,5)
        apartamentController.addBill(3,BillType.Water,100)
        apartamentController.addBill(4,BillType.Water,100)
        apartamentController.addBill(4,BillType.Water,5)
        apartamentController.deleteAllBillsFromApartamentsInRange(2,3)
        self.assertEqual(len(apartamentController.all[2].bills),0)
        self.assertEqual(len(apartamentController.all[3].bills),0)
        self.assertEqual(len(apartamentController.all[4].bills),2)

    def testGetBillsCostOfType(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Gas,10)
        apartamentController.addBill(1,BillType.Water,100)
        apartamentController.addBill(1,BillType.Gas,10)
        apartamentController.addBill(2,BillType.Water,100)
        apartamentController.addBill(2,BillType.Water,5)
        apartamentController.addBill(3,BillType.Gas,80)
        apartamentController.addBill(4,BillType.Water,100)
        apartamentController.addBill(4,BillType.Water,5)
        self.assertEqual(apartamentController.getBillsCostOfType(BillType.Gas),100)

    def testUndo(self):
        apartamentController = ApartamentController()
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.undo()
        self.assertEqual(apartamentController.getBillsCostOfType(BillType.Water),0)
        apartamentController.addBill(0,BillType.Water,50)
        apartamentController.addBill(0,BillType.Water,100)
        apartamentController.addBill(0,BillType.Water,200)
        apartamentController.addBill(0,BillType.Water,300)
        apartamentController.undo()
        apartamentController.undo()
        self.assertEqual(apartamentController.getBillsCostOfType(BillType.Water),150)
if __name__ == '__main__':
    unittest.main()
