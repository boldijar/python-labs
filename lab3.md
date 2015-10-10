# Lab 3- Documentation

With this simple python script you can:

 * See a menu with options
 * read numbers
 * find out the longest sequence of numbers where the difference between all consecutive numbers is a prime number as well
 * find out the longest sequence of numbers where all the numbers are greater and equal than 0 and smaller or equal than 10.
 * exit the application


## See a menu with options
You can see the next menu:
```
1) Read numbers
2) Longest sequence of numbers where the difference of every 2 number is a prime number
3) Longest sequence of numbers where the numbers are in [0;10]
4) Exit application
Your option: 
```

Here you need to choose what option do you want, by writting the number of the option.
You can **only** use the numbers 1, 2, 3, 4.

## Read the numbers
First you need to read how many number you need, and those numbers.
You can only read integers from [-10000;10000].

## 1st exercise
If you choose the option #2 you will see a list of numbers which is the longest sequence of numbers where the difference of every consecutive numbers is a prime number (absolute number if first number is smaller than the second one).

Some examples:

| List          | Result           | Why  |
| ------------- |:-------------:| -----:|
| [1,2,3,4]      | [] | Difference between each 2 consecutive number is 1 (not prime)|
| [1,3,7,11,16    | [1,3,7]      |  Solutions: [1,3,7] and [11,16], first one is longer |
| [] | []      |    Empty list, no solution |

## 2nd exercise
If you choose the option #3 you will see a list of numbers which is the longest sequence of numbers that are in [0,10]

Some examples:

| List          | Result           | Why  |
| ------------- |:-------------:| -----:|
| [1,2,3,4]      | [1,2,3,4] | All numbers are in [0;10]|
| [1,3,7,11,3,4]    | [1,3,7]      |  Solutions: [1,3,7] and [3,4], first one is longer |
| [] | []      |    Empty list, no solution |

## Exit application
Choosing the last option will close the application.



