from bill import Bill
from bill_type import BillType

class Apartament:

    def __init__(self, bills,number):
        self.bills = bills
        self.number = number

    def __init__(self,number):
        self.bills = []
        self.number = number

    def addBill(self,bill):
        self.bills.append(bill)

class Apartaments:

    def __init__(self,all):
        self.all = all

    def __init__(self):
        self.all = []
        for i in range (0,100):
            apartament = Apartament(i)
            self.all.append(apartament)

    def getBillTypeName(self,position):
        if position == BillType.Water :
            return "Water"
        if position == BillType.Sewerage:
            return "Sewerage"
        if position == BillType.Gas:
            return "Gas"
        if position == BillType.Other:
            return "Other"
        return "error"

    def editBill(self,apartamentNumber,billIndex,newBillCost,newBillType):
        for i in range (0,len(self.all)):
            apartament = self.all[i]
            if apartament.number == apartamentNumber:
                apartament.bills[billIndex].cost=newBillCost
                apartament.bills[billIndex].type=newBillType
                
            
    def getAllApartamentsAndBills(self):
        result = ""
        for i in range (0,len(self.all)):
            apartament = self.all[i]
            for j in range (0,len(apartament.bills)):
                bill = apartament.bills[j]
                result = result + "Apartament #" + str(apartament.number)+ " , Bill id: "+str(j)+ " , type: "+self.getBillTypeName(bill.type) +" , cost: "+str(bill.cost) +"\n"            
        return result
    
    def get(self,index):
        return self.all[index]
    
    def getApartamentCost(self,apartamentIndex):
        cost = 0
        apartament = self.all[apartamentIndex]
        for i in range (0,len(apartament.bills)):
            cost = cost + apartament.bills[i].cost
        return cost

    def getApartamentsWithCostGreatherThan(self,cost):
        list = []
        for apartamentIndex in range(0,len(self.all)) :
            if getApartamentCost(apartamentIndex) > cost:
                list.append(self.all[apartamentIndex])
        return Apartaments(list)

    
    def getApartamentsCount(self):
        return len(self.all)

    def getCertainBillsFromAllApartaments(self,billType):
        list = []
        for i in range (0,len(self.all)):
            apartament= self.all[i]
            for j in range (0,len(apartament.bills)):
                bill = apartament.bills[j];
                if bill.type == billType:
                    list.append(bill)
    def getBillsCost(self,bills):
        cost = 0
        for i in range (0,len(bills)):
            cost = cost + bills[i].cost
        return cost

    def clearApartamentBills(self,apartamentIndex):
        self.all[apartamentIndex].bills = []

    def clearApartamentCertainBills(apartamentIndex,billType):
        apartament = self.all[apartamentIndex]
        for i in range (0,len(apartament.bills)):
            bill = apartament.bills[i]
            if bill.type == billType:
                bill.pop(i)
                i = i - 1
                
    def clearCertainBillsFromAllApartaments(self,billType):
        for apartamentIndex in range (0,len(self.all)):
            clearApartamentCertainBills(apartamentIndex,billType)
            
        

apartaments = Apartaments()

