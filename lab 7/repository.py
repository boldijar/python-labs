import json
from collections import namedtuple
from domain import *
class Repository:

    # converts this class to json
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,indent=4, separators=(',', ': '))

    # converts an object to json
    def objToJson(self,obj):
        return json.dumps(obj, default=lambda o: o.__dict__,indent=4, separators=(',', ': '))

    #saves to local json db
    def save(self):
        file = open("repository.db", "w")
        file.write(self.toJson())
        file.close()

    # reads from local json db
    def getJsonDb(self):
        file = open("repository.db", "r")
        return file.read()

    # loads from local json db into object
    def load(self):
        db = json.loads(self.getJsonDb(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.movieId = db.movieId
        self.clientId = db.clientId
        self.movies=[]
        self.clients=[]
        loadedMovies=db.movies
        for loadedMovie in loadedMovies:
            movie = Movie(loadedMovie.title,loadedMovie.description,loadedMovie.genre)
            movie.rentedTimes=loadedMovie.rentedTimes
            movie.rentedClientId = loadedMovie.rentedClientId
            movie.id = loadedMovie.id
            self.movies.append(movie)
            
        loadedClients=db.clients
        for loadedClient in loadedClients:
            client = Client(loadedClient.name,loadedClient.cnp)
            client.rentedBooksCount = loadedClient.rentedBooksCount
            client.id = loadedClient.id
            self.clients.append(client)


    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    # default constructor
    def __init__(self):
        self.clients = []
        self.movies = []
        self.movieId = 0
        self.clientId = 0

    # adds client
    def addClient(self,name,cnp):
        client = Client(name,cnp)
        client.id = self.clientId;
        self.clientId = self.clientId + 1
        self.clients.append(client)
        return client
    
    #adds a new movie
    def addMovie(self,title,description,genre):
        movie = Movie(title,description,genre)
        movie.id=self.movieId;
        self.movieId = self.movieId + 1
        self.movies.append(movie)
        return movie

    def deleteClient(self,clientId):
        somethingWasDeleted = False
        for client in self.clients:
            if client.id == clientId:
                self.clients.remove(client)
                somethingWasDeleted = True
        return somethingWasDeleted

    def deleteMovie(self,movieId):
        somethingWasDeleted = False
        for movie in self.movies:
            if movie.id == movieId:
                self.movies.remove(movie)
                somethingWasDeleted = True
        return somethingWasDeleted

    def updateClient(self,clientId,name,cnp):
        for client in self.clients:
            if client.id == clientId:
                client.name = name
                client.cnp = cnp

    def updateMovie(self,movieId,title,description,genre):
        for movie in self.movies:
            if movie.id == movieId:
                movie.title = title
                movie.description = description
                movie.genre = genre

