import sys


global lista
lista = []
global size

""" this function will show us the menu, and will return the option selected """
def showMenu():
    print '1) Read numbers'
    print '2) Properties 1'
    print '3) Properties 2'
    print '4) Exit application'
    return int(input('Your option: '))
    
""" this function will read the size and all the numbers and add it to the list"""
""" but first, we are going to empty the list """
def readNumbers():
    lista[:]=[]
    size=int(input('How many numbers? '))
    print 'Read your numbers! '
    for i in range(0,size):
        lista.append(int(input('')))

""" this method will return true if number is prime, false if not """
def numberIsPrime(n):
    if n == 1:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


""" this is the main loop, where you check for menu options """
while True:
    option = showMenu()
    if option == 1:
        readNumbers()
    if option == 4:
        sys.exit()
    
