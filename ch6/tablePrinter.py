# Table Printer practice project at the end of chapter 6

# Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table
# with each column right-justified. Assume that all the inner lists will contain the same number of strings. For
# example, the value could look like this:


def printTable(tableData):
    maxLen = list(map(getMaxLen, tableData))
    colLen = len(tableData[0])

    for i in range(colLen):
        for j in range(len(tableData)):
            if j == len(tableData)-1:
                endStr = '\n'
            else:
                endStr = ' '

            print(tableData[j][i].rjust(maxLen[j]), end=endStr)


def getMaxLen(x):
    maxLen = 0
    for item in x:
        maxLen = max(len(item), maxLen)

    return maxLen


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

