movieId = 0
clientId = 0

class Movie:

    def __init__(self,title,description,genre):
        self.title = title
        self.description = description
        self.genre = genre
        self.rentedTimes = 0
        self.rentedClientId = None
        global movieId
        self.id = movieId
        movieId = movieId + 1

class Client:

    def __init__(self,name,cnp):
        self.name = name
        self.cnp = cnp
        self.rentedBooksCount = 0
        global clientId
        self.id = clientId
        clientId = clientId + 1
