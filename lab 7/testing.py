import unittest
from controller import *
class TestController(unittest.TestCase):
    
    
    def testAddClient(self):
        controller = Controller()
        controller.addClient("Paul","12345")
        self.assertEqual(len(controller.repository.clients),1)
        
    def testAddMovie(self):
        controller = Controller()
        controller.addMovie("titanic","12345","drama")
        controller.addMovie("titanic","12345","drama")
        controller.addMovie("titanic","12345","drama")
        self.assertEqual(len(controller.repository.movies),3)

    def testDeleteClient(self):
        controller = Controller()
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        client3 = controller.addClient("Paulaa","1234522")
        client4 = controller.addClient("Paulaaa","1234533")
        client5 = controller.addClient("Paulaaaa","1234544")
        controller.deleteClient(client1.id)
        controller.deleteClient(client5.id)
        self.assertEqual(len(controller.repository.clients),3)

    def testDeleteMovie(self):
        controller = Controller()
        movie1 = controller.addMovie("titanic1","12345","drama")
        movie2 = controller.addMovie("titanic2","12345","drama")
        movie3 = controller.addMovie("titanic3","12345","drama")
        self.assertEqual(controller.deleteMovie(movie2.id),True)
        self.assertEqual(len(controller.repository.movies),2)

    def testUpdateClient(self):
        controller = Controller()
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        controller.updateClient(client1.id,"Dan","69")
        self.assertEqual(controller.repository.clients[0].name,"Dan")
        self.assertEqual(controller.repository.clients[0].cnp,"69")
    

    def testUpdateMovie(self):
        controller = Controller()
        movie1 = controller.addMovie("titanic1","12345","drama")
        movie2 = controller.addMovie("titanic2","12345","drama")
        movie3 = controller.addMovie("titanic3","12345","drama")
        controller.updateMovie(movie1.id,"Titlu","Desc","Comed")
        self.assertEqual(controller.repository.movies[0].title,"Titlu")
        self.assertEqual(controller.repository.movies[0].description,"Desc")
        self.assertEqual(controller.repository.movies[0].genre,"Comed")


    def testSearchClient(self):
        controller = Controller()
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        self.assertEqual(controller.searchForClient("Paul").id,client1.id)
        self.assertEqual(controller.searchForClient("Dan"),None)

    def testSearchMovie(self):
        controller = Controller()
        movie1 = controller.addMovie("mov","12345","drama")
        movie2 = controller.addMovie("mov3","12345","drama")
        self.assertEqual(controller.searchForMovie("mov").id,movie1.id)
        self.assertEqual(controller.searchForMovie("random"),None)

    def testSearchClientById(self):
        controller = Controller()
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        self.assertEqual(controller.searchForClientById(client1.id).name,"Paul")
        self.assertEqual(controller.searchForClientById(1290),None)

    def testSearchMovieById(self):
        controller = Controller()
        movie1 = controller.addMovie("mov","12345","drama")
        movie2 = controller.addMovie("mov3","12345","drama")
        self.assertEqual(controller.searchForMovieById(movie1.id).title,"mov")
        self.assertEqual(controller.searchForMovieById(1232),None)

    def testRentMovie(self):
        controller = Controller()
        movie1 = controller.addMovie("mov","12345","drama")
        movie2 = controller.addMovie("mov3","12345","drama")
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        self.assertEqual(controller.rentMovie(-100,200),False)
        self.assertEqual(controller.rentMovie(client1.id,movie1.id),True)
        self.assertEqual(controller.rentMovie(client1.id,movie1.id),False)
        self.assertEqual(controller.rentMovie(client1.id,movie2.id),True)
        self.assertEqual(movie1.rentedTimes,1)
        self.assertEqual(client1.rentedBooksCount,2)
        
    def testUnRentMovie(self):
        controller = Controller()
        movie1 = controller.addMovie("mov","12345","drama")
        movie2 = controller.addMovie("mov3","12345","drama")
        client1 = controller.addClient("Paul","123451")
        client2 = controller.addClient("Paula","1234511")
        controller.rentMovie(client1.id,movie1.id)
        self.assertEqual(controller.unRentMovie(movie2.id),False)
        self.assertEqual(controller.unRentMovie(movie1.id),True)
        self.assertEqual(controller.unRentMovie(1235),False)
        
if __name__ == '__main__':
    unittest.main()
