import json
from collections import namedtuple
from domain import *
class Repository:
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__,indent=4, separators=(',', ': '))
    
    def save(self):
        file = open("repository.db", "w")
        file.write(self.toJson())
        file.close()

    def getJsonDb(self):
        file = open("repository.db", "r")
        return file.read()

    def load(self):
        db = json.loads(self.getJsonDb(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        self.movieId = db.movieId
        self.clientId = db.clientId
        self.movies = db.movies
        self.clients = db.clients

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
    
    def __init__(self):
        self.clients = []
        self.movies = []
        self.movieId = 0
        self.clientId = 0

    def addClient(self,name,cnp):
        client = Client(name,cnp)
        client.id = self.clientId;
        self.clientId = self.clientId + 1
        self.clients.append(client)
        return client

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

