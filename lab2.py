def readNumber():
    return int(input('Read number '))

def maxNumber(number):
    freq=[0,0,0,0,0,0,0,0,0,0]
    while number > 0:
        freq[number%10] = freq[number%10] + 1
        number = number / 10

    for i in range (9,-1,-1):
        while freq[i] > 0:
            number = number * 10 + i
            freq[i] = freq[i] - 1
    return number

def main():
    number = readNumber()
    print 'Maximum number is : ',maxNumber(number)


main()
