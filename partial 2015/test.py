import unittest
from controller import *
class test(unittest.TestCase):
    
    def test_random(self):
        self.assertEquals(1,1)

    def test_repository_add(self):
        repo = RepositoryAlimente()
        repo.addAliment(Aliment("Da",1,2))
        self.assertEquals(1,len(repo.getAll()))
        

    def test_repository_actualizeaza(self):
        repo = RepositoryAlimente()
        repo.addAliment(Aliment("Da",2,2))
        repo.addAliment(Aliment("Nu",2,2))
        repo.addAliment(Aliment("Hm",2,2))

        self.assertEquals(repo.actualizeazaCantitate("Da",10),False)
        self.assertEquals(repo.actualizeazaCantitate("Nu",2),True)
        self.assertEquals(repo.getAll()[1].getCantitate(),0)

    def test_controller_actualizeaza(self):
        con = ControllerAlimente()
        con.getRepo().addAliment(Aliment("Da",2,2))
        con.getRepo().addAliment(Aliment("Nu",2,2))
        con.getRepo().addAliment(Aliment("Hm",2,2))

        self.assertEquals(con.actualizeazaCantitate("Da",10),False)
        self.assertEquals(con.actualizeazaCantitate("Nu",2),True)
        self.assertEquals(con.getRepo().getAll()[1].getCantitate(),0)

    def test_controller_fltru(self):
        con = ControllerAlimente()
        con.getRepo().addAliment(Aliment("F",10,4))
        con.getRepo().addAliment(Aliment("Z",10,5))
        con.getRepo().addAliment(Aliment("A",10,1))
        con.getRepo().addAliment(Aliment("Yolo",10,7))

        lista= con.filtrareDupaZilePanaLaExpirare(5)

        self.assertEquals(lista[0].getNume(),"A")
        self.assertEquals(lista[1].getNume(),"F")
        self.assertEquals(lista[2].getNume(),"Z")

    def test_file_read(self):
        repo=RepositoryAlimente()
        repo.loadFromFile("test.txt")
        self.assertEquals(len(repo.getAll()),4)
        
        
if __name__ == '__main__':
    unittest.main()
