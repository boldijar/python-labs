from controller import *

controller = Controller()
controller.repository.load()
controller.repository.save()


def show_movies():
    for movie in controller.repository.movies:
        print 'Id: ' + str(movie.id)+ ' Title: ' + movie.title + ' Description: ' + movie.description + ' Genre: '+movie.genre

def show_clients():
    for client in controller.repository.clients:
        print 'Id:'+str(client.id)+' Name:'+client.name + ' CNP: '+client.cnp;

def add_movie():
    input = raw_input('Follow this pattern: Title,Description,genre : ')
    fields = input.split(',')
    if len(fields) != 3 :
        print 'Invalid input'
        return;
    controller.repository.addMovie(fields[0],fields[1],fields[2])
    controller.repository.save()

def add_client():
    input = raw_input('Follow this pattern: Name,Cnp : ')
    fields = input.split(',')
    if len(fields) != 2 :
        print 'Invalid input'
        return;
    controller.repository.addClient(fields[0],fields[1])
    controller.repository.save()

def delete_client():
    id = raw_input('Client id: ')
    if validateInt(id) == False:
        print 'Invalid id'
        return
    id=int(id)
    deleted = controller.repository.deleteClient(id)
    if deleted == True:
        print 'Client deleted.'
        controller.repository.save()
    else:
        print 'No client found'

def delete_movie():
    id = raw_input('Movie id: ')
    if validateInt(id) == False:
        print 'Invalid id'
        return
    id=int(id)
    deleted = controller.repository.deleteMovie(id)
    if deleted == True:
        print 'Movie deleted.'
        controller.repository.save()
    else:
        print 'No movie found'

def search_client():
    name = raw_input('Client name: ')
    client = controller.searchForClient(name)
    if client == None:
        print 'No client found.'
    else:
        print 'Id:'+str(client.id)+' Name:'+client.name + ' CNP: '+client.cnp;

def sort():
    print 'Read numbers untill 0: '
    list = []
    while True:
        value = raw_input('')
        value = int(value)
        if value == 0:
            print controller.sort(list)
            return
        list.append(value)
        
            

def search_movie():
    title = raw_input('Movie title: ')
    movie = controller.searchForMovie(title)
    if movie == None:
        print 'No movie found.'
    else:
        print 'Id: ' + str(movie.id)+ ' Title: ' + movie.title + ' Description: ' + movie.description + ' Genre: '+movie.genre

def rent_movie():
     

    clientId = raw_input('Client id: ')
    if validateInt(clientId) == False:
        print 'Invalid client id'
        return
    clientId=int(clientId)

    movieId = raw_input('Movie id: ')
    if validateInt(movieId) == False:
        print 'Invalid movie id'
        return
    movieId=int(movieId)
    
    result = controller.rentMovie(clientId,movieId)
    if result ==0 :
        print 'At least one of the ids are not valid'
    if result == 1:
        print 'Movie is already rented'
    if result == 2:
        print 'Movie successfully rented!'
        controller.repository.save()

def unrent_movie():
    movieId= int(input('Movie id: '))
    result = controller.unRentMovie(movieId)
    if result == 0:
        print 'Movie id invalid'
    if result == 1:
        print 'Movie is not rented'
    if result == 2:
        print 'Movie successfully unrented!'
        controller.repository.save()

def clients_30percent():
    list = controller.getFirst30PerCentClients()
    for client in list:
        print 'Id:'+str(client.id)+' Name:'+client.name + ' Rented books: '+str(client.rentedBooksCount);
    
def movies_sorted_by_rent():
    list = controller.getSortedMoviesByRentedTimes()
    for movie in list:
        print 'Id: ' + str(movie.id)+ ' Title: ' + movie.title + ' Description: ' + movie.description + ' Genre: '+movie.genre

    
def validateInt(text):
    try:
        text=int(text)
        return True
    except:
        return False

def validateString(text,count):
    list = text.split(',')
    return len(list) == count
        
def show_menu():
    print '0) Quit'
    print '1) Show clients'
    print '2) Show movies'
    print '3) Add client'
    print '4) Add movie'
    print '5) Delete client'
    print '6) Delete movie'
    print '7) Find client'
    print '8) Find movie'
    print '9) Rent movie'
    print '10) Unrent movie'
    print '11) First 30 percent of clients with most rented books'
    print '12) Movies sorted by rented times'
    print '13) Sort array'
    inp=raw_input('Option: ')
    if validateInt(inp) == False:
        print 'Invalid option'
        return -1
    return  int(inp)
  

while True:
    option = show_menu()
    if option == 0:
        break
    if option == 1:
        show_clients()
    if option == 2:
        show_movies()
    if option == 3:
        add_client()
    if option == 4:
        add_movie()
    if option == 5:
        delete_client()
    if option == 6:
        delete_movie()
    if option ==7:
        search_client()
    if option ==8:
        search_movie()
    if option ==9:
        rent_movie()
    if option ==10:
        unrent_movie()
    if option ==11:
        clients_30percent()
    if option ==12:
        movies_sorted_by_rent()
    if option == 13:
        sort()

#controller.repository.save()
