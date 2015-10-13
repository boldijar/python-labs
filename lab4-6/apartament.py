from bill import Bill

class Apartament:

    def __init__(self, bills,number):
        self.bills = bills
        self.number = number

    def __init__(self,number):
        self.bills = []
        self.number = number

class Apartaments:

    def __init__(self):
        self.all = []
        for i in range (0,100):
            apartament = Apartament(i)
            self.all.append(apartament)

    def getApartamentCost(self,apartamentIndex):
        cost = 0
        apartament = self.all[apartamentIndex]
        for i in range (0,len(apartament.bills)):
            cost = cost + apartament.bills[i].cost
        return cost

    def getApartamentsCount(self):
        return len(self.all)

apartaments = Apartaments()

print apartaments.getApartamentCost(2)
      
