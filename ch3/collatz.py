# Practice project at the end of Chapter 3

# Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print
# number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1.

# Add try and except statements to the previous project to detect whether the user types in a noninteger string

def collatz(number):
    if number % 2 == 0:
        newNumber = number // 2
    else:
        # number is odd
        newNumber = 3 * number + 1

    print(newNumber)
    return newNumber


try:
    inputStr = input('Pick an integer to start at: ')
    intStart = int(inputStr)

    curNum = intStart
    while curNum != 1:
        curNum = collatz(curNum)
except ValueError:
    print('Must enter an integer. You entered: ' + inputStr)

