from bicicleta import bicicleta
class repository:
    def __init__(self):
        self.biciclete=[]

    def add_bicicleta(self,id,tip,pret):
        bicicletaa=bicicleta(id,tip,pret)
        self.biciclete.append(bicicletaa)
        
    def get_all(self):
        return self.biciclete
    def delete(self,id):
        for bicicleta in self.biciclete:
            if id==bicicleta.id:
                self.biciclete.remove(bicicleta)


    def incarca_din_fisier(self):
        with open("biciclete.txt") as fisier:
            linii = fisier.readlines()
            for linie in linii:
                valori = linie.split(',')
                id = int(valori[0])
                tip = valori[1]
                pret =float(valori[2])
                self.add_bicicleta(id,tip,pret)

    def salveaza(self):
        fisier = open("biciclete.txt","w")
        for bicicleta in self.get_all():
            fisier.write(str(bicicleta.id) + ',' + bicicleta.tip + "," + str(bicicleta.pret))
            fisier.write('\n')
        fisier.close()

    
        
       
