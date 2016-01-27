from controller import controller

con = controller()
con.loadFromFile()

def showMenu():
    print '1)Adauga cuvant'
    print '2)Sterge cuvant'
    print '3)Traduce text din fisier'
    return raw_input('Alegerea ta: ')



def adaugaCuvant():
    limbaSursa = raw_input('Limba sursa: ')
    cuvant = raw_input('Cuvant: ')
    limbaDestinatie = raw_input('Limba destinatie: ')
    traducerea = raw_input('Traducere: ')

    rez = con.addTraducere(limbaSursa,cuvant,limbaDestinatie,traducerea)
    if rez.succes == False:
        print rez.mesaj
    else:
        print 'Traducere adaugata'
        con.save()

def stergeCuvant():
    cuvant=raw_input('Cuvant: ')

    rez=con.stergeTraducere(cuvant)
    if rez.succes == False:
        print rez.mesaj
    else:
        print 'Cuvant sters'
        con.save()

def traduceFisier():
    numeFisierIntrare = raw_input('Nume fisier intrare: ')
    limbaSursa=raw_input('Limba sursa: ')
    numeFisierIesire = raw_input('Nume fisier iesire: ')
    limbaDest=raw_input('Limba destinatie: ')

    con.traduceDinFisier(numeFisierIntrare,numeFisierIesire,limbaSursa,limbaDest)
    print 'Gata.'
while True:
    optiune=showMenu()
    if optiune == "1":
        adaugaCuvant()
    if optiune == "2":
        stergeCuvant()
    if optiune == "3":
        traduceFisier()
    
    
