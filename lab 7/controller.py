from repository import *
from domain import *
class Controller:

    def __init__(self):
        self.repository = Repository()

    def addClient(self,name,cnp):
        client = Client(name,cnp)
        self.repository.clients.append(client)
        return client

    def addMovie(self,title,description,genre):
        movie = Movie(title,description,genre)
        self.repository.movies.append(movie)
        return movie

    def deleteClient(self,clientId):
        somethingWasDeleted = False
        for client in self.repository.clients:
            if client.id == clientId:
                self.repository.clients.remove(client)
                somethingWasDeleted = True
        return somethingWasDeleted

    def deleteMovie(self,movieId):
        somethingWasDeleted = False
        for movie in self.repository.movies:
            if movie.id == movieId:
                self.repository.movies.remove(movie)
                somethingWasDeleted = True
        return somethingWasDeleted

    def updateClient(self,clientId,name,cnp):
        for client in self.repository.clients:
            if client.id == clientId:
                client.name = name
                client.cnp = cnp

    def updateMovie(self,movieId,title,description,genre):
        for movie in self.repository.movies:
            if movie.id == movieId:
                movie.title = title
                movie.description = description
                movie.genre = genre

    def searchForMovie(self,movieTitle):
        for movie in self.repository.movies:
            if movie.title == movieTitle:
                return movie
        return None

    def searchForClient(self,clientName):
        for client in self.repository.clients:
            if client.name == clientName:
                return client
        return None

    def searchForMovieById(self,movieId):
        for movie in self.repository.movies:
            if movie.id == movieId:
                return movie
        return None

    def searchForClientById(self,clientId):
        for client in self.repository.clients:
            if client.id == clientId:
                return client
        return None
    
    def rentMovie(self,clientId,movieId):
        movie = self.searchForMovieById(movieId)
        client = self.searchForClientById(clientId)
        if movie == None or client == None:
            return False
        if movie.rentedClientId != None:
            return False
        movie.rentedTimes = movie.rentedTimes + 1
        client.rentedBooksCount = client.rentedBooksCount +1
        movie.rentedClientId = client.id
        return True

    def unRentMovie(self,movieId):
        movie = self.searchForMovieById(movieId)
        if movie == None:
            return False
        if movie.rentedClientId == None:
            return False
        movie.rentedClientId = None
        return True

    def getSortedMoviesByRentedTimes(self):
        self.repository.movies.sort(key = lambda x: x.rentedTimes, reverse = True)
        return self.repository.movies
    
    def getSortedClientsByMoviesRented(self):
        self.repository.clients.sort(key = lambda x: x.rentedBooksCount,reverse = True)
        return self.repository.clients

    def getFirst30PerCentClients(self):
        sortedClients=self.getSortedClientsByMoviesRented()
        list = []
        totalClients = len(self.repository.clients)
        count = int(30/100.0*totalClients)
        for i in range(0,count):
            list.append(sortedClients[i])
        return list
            

    
