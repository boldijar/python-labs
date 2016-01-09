

lista_principala = []
stiva = []

lista_principala = [1,2,3,4]

n = len(lista_principala)
for i in range (0,n):
    stiva.append(0)


def lista_e_munte(lista):
    creste = True
    scade = False
    gasitPrimaParte = False

    if len(lista) < 3:
        return False
            
    for i in range(0,len(lista)-1):
        j = i+1
        if creste:
            if lista[j]<lista[i]:
                creste = False
                scade = True
            if lista[j]>lista[i]:
                gasitPrimaParte = True
        if scade:
            if lista[i] < lista[j]:
                return False

    if gasitPrimaParte == False:
        return False
    if lista[len(lista)-1] > lista[len(lista)-2]:
        return False
    
    return True

def afisare_lista(lista):
    mesaj = ""
    for nr in lista:
        mesaj = mesaj + str(nr)+" "
    print mesaj

def valid(k):
    for i in range(0,k):
        if stiva[k] == stiva[i]:
            return False
        #print 'hmm: '+str(stiva)
    return True
def stiva_e_munte(k):
    lista = stiva_in_lista(k)
    stiva = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range ( 0, len(lista)):
        stiva [lista[i]] = stiva[lista[i]] + 1
    for i in range (0,len(lista)):
        if stiva[lista[i]] > 1:
            return
    return lista_e_munte(lista)
def stiva_in_lista(k):
    lista = []
    for i in range (0,k+1):
        lista.append(lista_principala[stiva[i]])
    return lista
def afisare(k):
    if stiva_e_munte(k):
        afisare_lista(stiva_in_lista(k))
        

def back(k):
    if k == n:
        return
    for i in range(0,n):
        stiva[k]=i;
        if valid(k):    
            afisare(k)
        back(k+1)
        
        
back(0)

