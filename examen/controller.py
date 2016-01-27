from model import *
from repository import *

class controller:

    def __init__(self):
        self.repo=repository()

    #salveaza repositoryul
    def save(self):
        self.repo.save()

    #incarca din fisier traducerile
    def loadFromFile(self):
        self.repo.loadFromFile()

    #adauga traducere, si verifica daca sunt ok parametrii
    #returnam obiectul rezultat, cu eroare in mesaj si succes false daca exista, altfel succes true
    def addTraducere(self,limbaSursa,cuvant,limbaDest,traducerea):
        rez = rezultat(False,"","")
        limbe="En","Ro","Fr"
        if not limbaSursa in limbe:
            rez.succes= False
            rez.mesaj = "Limba sursa invalida"
            return rez
        if not limbaDest in limbe:
            rez.succes= False
            rez.mesaj = "Limba destinatie invalida"
            return rez
        if limbaSursa == limbaDest:
            rez.succes= False
            rez.mesaj = "Limba sursa e aceasi ca si limba destinatie"
            return rez
        if len(str(cuvant)) == 0 or len(str(traducere))==0:
            rez.succes= False
            rez.mesaj = "Unul dintre cuvinte sau amandoua sunt goale"
            return rez
        for trad in self.repo.traduceri:
            if trad.limbaDest == limbaDest and trad.cuvantul==cuvant:
                rez.succes= False
                rez.mesaj = "Avem deja cuvantul tradus"
                return rez
        
        trad=traducere(limbaSursa,cuvant,limbaDest,traducerea)
        self.repo.traduceri.append(trad)
        rez.succes=True
        return rez

    #sterge fiecare traducere de unde apare cuvantul dorit
    def stergeTraducere(self,cuvant):
        rez = rezultat(False,"","")
        tradList = []
        for trad in self.repo.traduceri:
            if not(trad.cuvantul == cuvant or trad.traducerea == cuvant):
                tradList.append(trad)
        if len(self.repo.traduceri) == len(tradList):
            rez.succes = False
            rez.mesaj = "Nu a fost gasit cuvantul dorit"
            return rez
        rez.succes=True
        self.repo.traduceri=tradList
        return rez

    #se cauta in repo un cuvant cu limba sursa dorita, si se returneaza traducerea
    #in limba destinatie dorita, daca nu exista, se va returna ""
    def cautaTraducerea(self,cuvant,limbaSursa,limbaDestinatie):
        for trad in self.repo.traduceri:
            if trad.cuvantul == cuvant and trad.limbaSursa == limbaSursa and trad.limbaDest == limbaDestinatie:
                return trad.traducerea
        return ""

    #traduce textul din limba sursa in limba destinatie, daca nu gasim traducerea
    #unui cuvant, punem {cuvant}
    def traduceText(self,text,limbaSursa,limbaDestinatie):
        final=""
        cuvinte=text.split(' ')
        index = 0
        
        for cuvant in cuvinte:
            trad=self.cautaTraducerea(cuvant,limbaSursa,limbaDestinatie)
            if trad == "":
                final = final + "{"+cuvant+"}"
            else:
                final = final + trad
            if index < len(cuvinte)-1:
                final = final + " "
            index = index + 1
        return final

    #traduce textul din fisierul de intrare in fisierul de iesire din limba sursa in limba destinatie dorita
    def traduceDinFisier(self,numeFisierIntrare,numeFisierIesire,limbaSursa,limbaDestinatie):
        intrare=open(numeFisierIntrare,"r")
        textIntrare=intrare.read()
        linii = textIntrare.split('\n')
        rezultatul = ""
        for linie in linii:
            if len(str(linie)) > 0:
                rezultatul= rezultatul + self.traduceText(linie,limbaSursa,limbaDestinatie)+' '
            else:
                rezultatul = rezultatul + '\n'
            rezultatul = rezultatul +'\n'
            
        iesire=open(numeFisierIesire,"w")
        iesire.write(rezultatul)
        iesire.close()
        intrare.close()
