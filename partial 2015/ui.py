from controller import *

class UIFrigider:
    
    def __init__(self):
        self.__ctrl=ControllerAlimente()
        self.__ctrl.getRepo().loadFromFile("a")


    def filtrare(self):
        nrzile=raw_input('Numar zile: ')
        try:
            nrzile = int(nrzile)
            lista = self.__ctrl.filtrareDupaZilePanaLaExpirare(nrzile)
            if len(lista) == 0:
                print 'Nu exista niciun aliment din pacate'
                return
            for aliment in lista:
                print aliment.getNume(),' expira in ',aliment.getNrZile(),' zile'
        except:
            print 'Valoarea introdusa este invalida'
    
    def actualizare(self):
        nume = raw_input('Nume aliment: ')
        cantitate = raw_input('Cantitate: ')
        try:
            cantitate = int(cantitate)
            actualizat=self.__ctrl.actualizeazaCantitate(nume,cantitate)
            if actualizat:
                print 'Actualizat cu success!'
            else:
                print 'Nu a fost actualizat. Cantitate insuficienta'

        except:
            print 'Valoarea introdusa pentru cantitate e invalida.'
        
    def showMenu(self):
        print '1)Filtrare dupa zile pana la expirare'
        print '2)Actualizeaza cantitate'
        print '3)Iesire'

        result = raw_input('Optiune: ')
        try:
            result = int(result)
            if result <1 or result >3:
                print 'Valoare invalida.'
                return 0
            return result
        except:
            print 'Valoare invalida.'
            return 0

    def start(self):
        while True:
            optiune = self.showMenu()
            if optiune == 1:
                self.filtrare()
            if optiune == 2:
                self.actualizare()
            if optiune == 3:
                break

UIFrigider().start()
            

    


