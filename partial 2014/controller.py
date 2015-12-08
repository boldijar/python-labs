from repository import *
class controller:
    def __init__(self):
        self.repo=repository()

    def sterge_biciclete_tip(self,tip):
        for bicicleta in self.repo.get_all()[:]:
            if tip==bicicleta.tip:
                self.repo.delete(bicicleta.id)
                
    def calculeaza_max(self):
        pret_maxim = 0
        for bicicleta in self.repo.get_all():
            if bicicleta.pret > pret_maxim:
                pret_maxim=bicicleta.pret
        return pret_maxim

    def sterge_max(self):
        pret_maxim=self.calculeaza_max()
        for bicicleta in self.repo.get_all()[:]:
            if bicicleta.pret==pret_maxim:
                self.repo.delete(bicicleta.id)
                
        
