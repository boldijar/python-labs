from model import traducere

class repository:


    #constructorul clasei va initializa lista de traduceri
    def __init__(self):
        self.traduceri=[]

    #metoda va incarca in lista de traduceri, ce avem in fisier
    def loadFromFile(self):
        fisier = open("database.txt","r")
        continut = fisier.read()
        lines= continut.split('\n')
        for line in lines:
            if len(line) > 0:                
                data = line.split(',')
                trad=traducere(data[0],data[1],data[2],data[3])
                self.traduceri.append(trad)
        fisier.close()

    #metoda aceasta va salva repositoryul
    def save(self):
        fisier = open("database.txt","w")
        output = ""
        for trad in self.traduceri:
            output = output + trad.limbaSursa+","+trad.cuvantul+","+trad.limbaDest+","+trad.traducerea
            output = output+'\n'
        fisier.write(output)
        fisier.close()
            
        
            
        


 
