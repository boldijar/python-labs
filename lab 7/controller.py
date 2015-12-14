from repository import *
from domain import *
from pydoc import help
class Controller:

    def __init__(self):
        self.repository = Repository()

    # will search for a movie with the chosen title
    def searchForMovie(self,movieTitle):
        for movie in self.repository.movies:
            if movie.title == movieTitle:
                return movie
        return None
    # will search for a client with the chosen name
    def searchForClient(self,clientName):
        for client in self.repository.clients:
            if client.name == clientName:
                return client
        return None
    
    # will search for a movie by a chosen id
    def searchForMovieById(self,movieId):
        return self.searchForMovieByIdRecursive(0,movieId)
        #for movie in self.repository.movies:
        #   if movie.id == movieId:
        #        return movie
        #return None

    def searchForMovieByIdRecursive(self,index,movieId):
        if index == len(self.repository.movies):
            return None
        if self.repository.movies[index].id == movieId:
            return self.repository.movies[index]
        return self.searchForMovieByIdRecursive(index + 1, movieId)

    # will search for a client by id
    def searchForClientById(self,clientId):
        return self.searchForClientByIdRecursive(0,clientId)
        #for client in self.repository.clients:
        #    if client.id == clientId:
        #        return client
        #return None

    def searchForClientByIdRecursive(self,index,clientId):
        if index == len(self.repository.clients):
            return None
        if self.repository.clients[index].id == clientId:
            return self.repository.clients[index]
        return self.searchForClientByIdRecursive(index + 1, clientId)

    #will rent the movie with the selected id, by the client with selected id
    def rentMovie(self,clientId,movieId):
        movie = self.searchForMovieById(movieId)
        client = self.searchForClientById(clientId)
        if movie == None or client == None:
            return 0
        if movie.rentedClientId != None:
            return 1
        movie.rentedTimes = movie.rentedTimes + 1
        client.rentedBooksCount = client.rentedBooksCount +1
        movie.rentedClientId = client.id
        return 2

    #will unrent the movie with the id selected
    def unRentMovie(self,movieId):
        movie = self.searchForMovieById(movieId)
        if movie == None:
            return 0
        if movie.rentedClientId == None:
            return 1
        movie.rentedClientId = None
        return 2

    # will sort the movies by how many times was rented, and return them
    def getSortedMoviesByRentedTimes(self):
        self.repository.movies.sort(key = lambda x: x.rentedTimes, reverse = True)
        return self.repository.movies

    # will sort the clients by how many movies they rented
    def getSortedClientsByMoviesRented(self):
        self.repository.clients.sort(key = lambda x: x.rentedBooksCount,reverse = True)
        return self.repository.clients
    # will return first 30% of clients that rented movies.
    def getFirst30PerCentClients(self):
        sortedClients=self.getSortedClientsByMoviesRented()
        list = []
        totalClients = len(self.repository.clients)
        count = int(30/100.0*totalClients)
        for i in range(0,count):
            list.append(sortedClients[i])
        return list
            

    
