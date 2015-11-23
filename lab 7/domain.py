

class Movie:

    def __init__(self,title,description,genre):
        self.title = title
        self.description = description
        self.genre = genre
        self.rentedTimes = 0
        self.rentedClientId = None
    

class Client:

    def __init__(self,name,cnp):
        self.name = name
        self.cnp = cnp
        self.rentedBooksCount = 0
    
