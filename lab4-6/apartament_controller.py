from bill import Bill
from bill_type import BillType
import copy

class Apartament:

    def __init__(self, bills,number):
        self.bills = bills
        self.number = number

    def __init__(self,number):
        self.bills = []
        self.number = number

    def addBill(self,bill):
        self.bills.append(bill)

class ApartamentController:

    def __init__(self,all):
        self.all = all
        self.oldAlls= []
        self.oldApartament= self

    # adds the current apartaments to a list
    def addToBackStack(self):
        self.oldAlls.append(copy.deepcopy(self.all))

    def undo(self):
        if(len(self.oldAlls) > 0):
            self.all=self.oldAlls[len(self.oldAlls)-1]
            self.oldAlls.pop(len(self.oldAlls)-1)
        
    def __init__(self):
        self.oldAlls = []
        self.all = []
        for i in range (0,100):
            apartament = Apartament(i)
            self.all.append(apartament)
        self.oldApartament=self

    def addBill(self,apartamentNumber,billType,billCost):
        self.addToBackStack()
        bill = Bill(billType,billCost)
        self.get(apartamentNumber).addBill(bill)

        
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
    # will delete all apartaments with id in range of leftIndex & rightIndex
    def deleteAllBillsFromApartamentsInRange(self,leftIndex,rightIndex):
        self.addToBackStack()
        for i in range(leftIndex,rightIndex+1):
            self.clearApartamentBills(i)
        
    def editBill(self,apartamentNumber,billIndex,newBillCost,newBillType):
        self.addToBackStack()
        for i in range (0,len(self.all)):
            apartament = self.all[i]
            if apartament.number == apartamentNumber:
                apartament.bills[billIndex].cost=newBillCost
                apartament.bills[billIndex].type=newBillType
                
        # will return a string with all apartaments and bills    
    def getAllApartamentsAndBills(self):
        result = ""
        for i in range (0,len(self.all)):
            apartament = self.all[i]
            for j in range (0,len(apartament.bills)):
                bill = apartament.bills[j]
                result = result + "Apartament #" + str(apartament.number)+ " , Bill id: "+str(j)+ " , type: "+self.getBillTypeName(bill.type) +" , cost: "+str(bill.cost) +"\n"            
        return result

    # will return an apartament
    def get(self,index):
        return self.all[index]
    
    def getApartamentCost(self,apartamentIndex):
        cost = 0
        apartament = self.all[apartamentIndex]
        for i in range (0,len(apartament.bills)):
            cost = cost + apartament.bills[i].cost
        return cost
    #returns a list of apartaments where the bill cost is > the cost selected
    def getApartamentsWithCostGreatherThan(self,cost):
        list = []
        for apartamentIndex in range(0,len(self.all)) :
            if self.getApartamentCost(apartamentIndex) > cost:
                list.append(self.all[apartamentIndex])
        return list

    def getApartamentsWithCostGreatherThanAsString(self,cost):
        result = ""
        apartaments = self.getApartamentsWithCostGreatherThan(cost)
        for i in range (0,len(apartaments)):
            result = result + "Apartament #"+str(apartaments[i].number)+" , cost: "+str(self.getApartamentCost(apartaments[i].number)) +"\n" 
        return result
        
    
    def getApartamentsCount(self):
        return len(self.all)
    # will return all bills of some type from all apartaments
    def getCertainBillsFromAllApartaments(self,billType):
        list = []
        for i in range (0,len(self.all)):
            apartament= self.all[i]
            for j in range (0,len(apartament.bills)):
                bill = apartament.bills[j];
                if bill.type == billType:
                    list.append(bill)
        return list
    def getCertainBillsFromAllApartamentsString(self,billType):
        list = self.getCertainBillsFromAllApartaments(billType)
        result= "Bills of type "+str(self.getBillTypeName(billType))+": \n"
        for bill in list[:]:
            result = result + "Cost: "+str(bill.cost)
            result = result +"\n"
        return result


    def getBillsCostOfType(self,billType):
        cost = 0
        for i in range (0,len(self.all)):
            app = self.all[i]
            for j in range(0,len(app.bills)):
                bill = app.bills[j]
                if bill.type == billType:
                    cost = cost + bill.cost
        return cost
    
    def getBillsCost(self,bills):
        cost = 0
        for i in range (0,len(bills)):
            cost = cost + bills[i].cost
        return cost

    def clearApartamentBills(self,apartamentIndex):
        self.all[apartamentIndex].bills = []
    # will delete certain bills from selected apartament
    def clearApartamentCertainBills(self,apartamentIndex,billType):
        apartament = self.all[apartamentIndex]
        for bill in apartament.bills[:]:
            if bill.type == billType:
                apartament.bills.remove(bill)
                
                
    def clearCertainBillsFromAllApartaments(self,billType):
        self.addToBackStack()
        for apartamentIndex in range (0,len(self.all)):
            self.clearApartamentCertainBills(apartamentIndex,billType)
            
        
