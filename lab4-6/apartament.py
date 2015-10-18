from bill import Bill

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

