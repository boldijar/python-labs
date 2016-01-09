

def lista_e_munte(lista):
    creste = True
    scade = False
    for i in range(0,len(lista)-1):
        j = i+1
        if creste:
            if lista[j]<lista[i]:
                creste = False
                scade = True
