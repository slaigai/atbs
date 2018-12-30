# Notes on assignment methods

# Multiple assignment
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat # number of variables and list len must be equal. else, ValueError
print(size, color, disposition)
# Multiple assignments to swap two variables
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

# Augmented Assignment Operators
i = 10
spam = 'Hello'
while i > 0:
    print(i)
    print(spam)
    i -= 1
    spam += spam




