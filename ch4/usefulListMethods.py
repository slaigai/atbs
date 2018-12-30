# Notes on useful list methods

# Finding index of item in list
spam = ['hello', 'hi', 'howdy', 'heyas', 'hello']
try:
    print(spam.index('hello')) # (0) returns first occurrence if duplicate
    print(spam.index('what?')) # (ValueError)
except ValueError:
    print('\'what?\' not found')

# Appending to a list
spam = []
for i in range(10):
    spam.append(i)
print(spam)

# Inserting into a list at position 1
spam.insert(1, 'new item')
print(spam)

# Remove new item from list (each call to remove only removes the first occurrence)
try:
    spam.remove('nonexistent element')
    print('removed nonexistent element')
except ValueError:
    spam.remove('new item')
    print('removed new item')

print(spam)

# Sorting a list
# Sort numbers in reverse order
spam.sort(reverse=True)
print(spam)
# Sort words in ASCIIbetical order
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)
# Sort letters in alphabetical order
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)