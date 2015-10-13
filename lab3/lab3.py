import sys
import webbrowser

""" this function will show us the menu, and will return the option selected """
def showMenu():
    print '\n\n'
    print '1) Read numbers'
    print '2) Longest sequence of numbers where the difference of every 2 number is a prime number'
    print '3) Longest sequence of numbers where the numbers are in [0;10]'
    print '4) Exit application'
    return int(input('Your option: '))
    
""" this function will read the size and all the numbers and add it to the list"""
""" but first, we are going to empty the list """
def readNumbers():
    list=[]
    size=int(input('How many numbers? '))
    print 'Read your numbers! '
    for i in range(0,size):
        list.append(int(input('')))
    return list

""" this method will return true if number is prime, false if not """
def numberIsPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True

""" this method will look for the longest sequence of numbers where
the difference of every 2 numbers is a prime number """
def properties1(list):
    maxLength = 0
    firstIndex = 0
    for i in range(0,len(list)) :
        """ searching for a sequence from the i index """
        currentLength = 0
        for j in range(i+1,len(list)):
            difference = abs(list[j] - list[j-1])
            if numberIsPrime(difference):
                currentLength = currentLength + 1
            else:
                break
            if currentLength > maxLength:
                firstIndex = i
                maxLength = currentLength
    if maxLength == 0:
        return list[firstIndex:firstIndex]
    return list[firstIndex:firstIndex + maxLength + 1]

""" this method will look for the longest sequence of numbers where all of them
are >=0 & <= 10"""        
def properties2(list):
    maxLength = 0
    firstIndex = 0
    for i in range(0,len(list)) :
        """ searching for a sequence from the i index """
        currentLength = 0
        for j in range(i,len(list)):
            if list[j] <= 10 and list[j] >= 0:
                currentLength = currentLength + 1
            else:
                break
            if currentLength > maxLength:
                firstIndex = i
                maxLength = currentLength

    return list[firstIndex:firstIndex + maxLength] 


""" this is the main loop, where you check for menu options """
def main():

    list = []
    while True:
        option = showMenu()
        if option == 1:
            list = readNumbers()
        if option == 2:
            print properties1(list)
        if option == 3:
            print properties2(list)
        if option == 4:
            sys.exit()


""" this method will prompt the user to read the documentation """
def showDocumentationMenu():
    print 'Do you want to go to the online documentation? Write Y if yes, if not, anything else.'
    answer = raw_input("Answer: ")
    if answer == ('y' or 'Y'):
        webbrowser.open('https://github.com/BoldijarPaul/python-labs/blob/master/lab3/lab3.md')

""" this method will check for errors, and call itself again """
def tryMain():
    try:
        main()
    except:
        print '\n\nI guess that you didn\'t used the numbers that you should.'
        showDocumentationMenu()
        tryMain()

tryMain()
