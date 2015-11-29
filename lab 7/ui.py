from Tkinter import *
from controller import *
root = Tk()                   

controller = Controller()
controller.repository.load()


    
movieListBox = Listbox(root)
clientListBox = Listbox(root)

def updateMovieListbox():
    for movie in controller.repository.movies:
        movieListBox.insert(0,movie.title)
    movieListBox.pack()
    
def updateClientListbox():
    print len(controller.repository.clients)
    for client in controller.repository.clients:
        clientListBox.insert(0,client.name)
    clientListBox.pack()
      
updateMovieListbox()
updateClientListbox()
                   
root.mainloop()  
