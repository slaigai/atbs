# Notes on dictionaries from Chapter 5

# Dictionaries are unordered
# Dicts cant be sliced

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('My cat has ' + myCat['color'] + ' fur.')

try:
    myCat['nonexistentKey']
except KeyError:
    print('Could not find key \'nonexistentKey\'')

