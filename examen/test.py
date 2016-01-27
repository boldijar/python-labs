import unittest
from controller import *
class TestController(unittest.TestCase):
    
    
    def test(self):
        self.assertEqual(1,1)

    def testAddTraducere(self):
        con=controller()
        self.assertEqual(con.addTraducere("Ro","cuv","En","bla").succes,True)
        self.assertEqual(con.addTraducere("Ro","cuv","En","bla").succes,False)
        self.assertEqual(con.addTraducere("Ro","cuv","Fr","bla").succes,True)
        self.assertEqual(con.addTraducere("Ro","","En","bla").succes,False)
        self.assertEqual(con.addTraducere("En","cuv","En","bla").succes,False)

    def testDeleteTraducere(self):
        con=controller()
        con.addTraducere("Ro","cuv","En","bla")
        con.addTraducere("Ro","abc","En","def")
        con.addTraducere("Ro","lala","En","baba")
        self.assertEqual(len(con.repo.traduceri),3)
        con.stergeTraducere("cuv")
        self.assertEqual(len(con.repo.traduceri),2)

        con2=controller()
        con2.addTraducere("Ro","cuv","En","bla")
        con2.addTraducere("Ro","abc","En","def")
        con2.addTraducere("Ro","lala","En","cuv")
        con2.stergeTraducere("cuv")
        self.assertEqual(len(con2.repo.traduceri),1)

    def testCautaTraducere(self):
        con=controller()
        con.addTraducere("Ro","om","En","man")
        con.addTraducere("Ro","abc","En","def")
        con.addTraducere("Ro","lala","En","baba")
        self.assertEqual(con.cautaTraducerea("om","Ro","En"),"man")        
        self.assertEqual(con.cautaTraducerea("omz","Ro","En"),"")

    def testFisier(self):
        con=controller()
        con.addTraducere("Ro","om","En","man")
        con.addTraducere("Ro","un","En","one")
        con.addTraducere("Ro","destept","En","smart")
        con.traduceDinFisier("test_intrare.txt","text_iesire.txt","Ro","En")
         
    def testTraducere(self):
        con=controller()
        text = "un om destept"
        text2 = "un om foarte destept"
        
        con.addTraducere("Ro","om","En","man")
        con.addTraducere("Ro","un","En","one")
        con.addTraducere("Ro","destept","En","smart")
        self.assertEqual(con.traduceText(text,"Ro","En"),"one man smart")
        self.assertEqual(con.traduceText(text2,"Ro","En"),"one man {foarte} smart")

    
if __name__ == '__main__':
    unittest.main()
