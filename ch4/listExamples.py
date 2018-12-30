# Notes on ways to work with lists

# List of lists
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

# Get second item in first list value (bat)
print(spam[0][1])

# Get last item in last list value (50)
print(spam[-1][-1])

# Slicing
# Get list slice, last three values from second list value ([30, 40, 50])
print(spam[1][-3:])
# Get list slice, all items except last item from second list value ([10, 20, 30, 40])
print(spam[1][0:-1])
# Slice assignment (prints [10, 1, 2, 3, 4])
spam[1][1:] = [1, 2, 3, 4]
print(spam[1])

# Length of list (5)
print(len(spam[1]))

# Concatenating lists (['cat', 'bat', 10, 1, 2, 3, 4])
spam = spam[0] + spam[1]
print(spam)
# Replicating lists ([1, 2, 3, 1, 2, 3, 1, 2, 3])
print([1, 2, 3]*3)

# Deleting list values (cat)
del spam[1:]
print(spam)


