from repository import *

class ControllerAlimente:
    def __init__(self):
        self.__repo=RepositoryAlimente()

    
    #returneza instata repositoriului
    def getRepo(self):
        return self.__repo
    # actualizeaza cantitatea daca se poate, si returneaza True, daca nu, False
    def actualizeazaCantitate(self,nume,cantitate):
        return self.__repo.actualizeazaCantitate(nume,cantitate)

    # cauta toate alimentele cu nrZile < = nrZile din parametru, si sorteaza dupa nume
    # nrzile trebuie sa fie un numar valid
    def filtrareDupaZilePanaLaExpirare(self,nrZile):
        lista  = []
        for aliment in self.__repo.getAll():
            if aliment.getNrZile() <= nrZile:
                lista.append(aliment)
        lista.sort(key = lambda x: x.getNume(),reverse = False)
        return lista
       


