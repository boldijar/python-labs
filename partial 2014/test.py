import unittest
from repository import *
from controller import *

class test(unittest.TestCase):

    def test_random(self):
        self.assertEquals(1,1)
    def test_add(self):
        repo=repository()
        repo.add_bicicleta(1,'tip',5)
        lungime=len(repo.get_all())
        self.assertEquals(lungime,1)

    def test_delete(self):
        repo=repository()
        repo.add_bicicleta(1,'tip',5)
        repo.add_bicicleta(5,'tip',5)
        repo.add_bicicleta(3,'tip',5)
        repo.delete(5)
        lungime=len(repo.get_all())
        self.assertEquals(lungime,2)
        
    def test_controller_delete_tip(self):
        ctrl=controller()
        ctrl.repo.add_bicicleta(1,'tip1',5)
        ctrl.repo.add_bicicleta(5,'tip2',5)
        ctrl.repo.add_bicicleta(9,'tip2',5)
        ctrl.sterge_biciclete_tip('tip2')
        lungime=len(ctrl.repo.get_all())
        self.assertEquals(lungime,1)

    def test_controller_sterge_max(self):
        ctrl=controller()
        ctrl.repo.add_bicicleta(1,'tip1',5)
        ctrl.repo.add_bicicleta(5,'tip2',588)
        ctrl.repo.add_bicicleta(9,'tip2',588)
        ctrl.repo.add_bicicleta(8,'tip2',150)
        ctrl.sterge_max()
        lungime=len(ctrl.repo.get_all())
        self.assertEquals(lungime,2)
    
if __name__ == '__main__':
    unittest.main()
