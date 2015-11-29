

class Movie:

    def __init__(self,title,description,genre):
        self.title = title
        self.description = description
        self.genre = genre
        self.rentedTimes = 0
        self.rentedClientId = None

    def text(self):
        print 'Id: ' + str(self.id)+ ' Title: ' + self.title + ' Description: ' + self.description + ' Genre: '+self.genre
    
class Client:

    def __init__(self,name,cnp):
        self.name = name
        self.cnp = cnp
        self.rentedBooksCount = 0

    def text(self):
        print 'Id:'+str(self.id)+' Name:'+self.name + ' CNP: '+self.cnp;

   
