# Example of passing args by reference to functions


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)
