from domain import *

class RepositoryAlimente:
    def __init__(self):
        self.__alimente = []

    #citeste din fisierul precizat
    #filename = text, numele fisierul de unde incarcam
    def loadFromFile(self,filename):
        self.__alimente = []
        with open(filename) as fisier:
            linii = fisier.readlines()
            for linie in linii:
                valori = linie.split(',')
                try:
                    nume = valori[0]
                    cantitate = int(valori[1])
                    nrZile=int(valori[2])
                    self.__alimente.append(Aliment(nume,cantitate,nrZile))
                except:
                    pass
                    
               
    # adauga un aliment
    # aliment este o instanta a clasei Aliment
    def addAliment(self,aliment):
        self.__alimente.append(aliment)
        
    #returneaza toate alimentele
    def getAll(self):
        return self.__alimente

    # actualizeaza cantitatea, returneaza True daca a fost actualizata, False daca nu e cantitatea suficienta
    # nume = string, cantitate = numar
    def actualizeazaCantitate(self,nume,cantitate):
        for aliment in self.__alimente[:]:
            if aliment.getNume() == nume:
                if cantitate > aliment.getCantitate():
                    return False
                else:
                    aliment.setCantitate(aliment.getCantitate()-cantitate)
        return True
                    

    
        
     

