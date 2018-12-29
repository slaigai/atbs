# Chapter 2, Question 9

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if
# anything else is stored in spam.

spam = input('Select a number to store in spam [1 or 2]')
print('You chose ' + spam)

if int(spam) == 1:
    print('Hello')
elif int(spam) == 2:
    print('Howdy')
else:
    print('Greetings!')
