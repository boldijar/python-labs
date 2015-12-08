class Aliment:
    def __init__(self,nume,cantitate,nr_zile):
        self.__nume=nume
        self.__cantitate=cantitate
        self.__nr_zile=nr_zile
        
    def getNume(self):
        return self.__nume

    def getCantitate(self):
        return self.__cantitate

    def getNrZile(self):
        return self.__nr_zile

    def setNume(self,nume):
        self.__nume=nume

    def setCantitate(self,cantitate):
        self.__cantitate=cantitate

    def setNrZile(self,nr_zile):
        self.__nr_zile=nr_zile
    


