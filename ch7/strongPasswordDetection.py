# Strong Password Detection Write a function that uses regular expressions to make sure the password string it is passed
# is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and
# lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to
# validate its strength.

import re


def isStrongPassword(password):
    isLongEnough = len(password) >= 8
    hasUpper = re.compile(r'[A-Z]+').search(password) is not None
    hasLower = re.compile(r'[a-z]+').search(password) is not None
    hasDigit = re.compile(r'\d+').search(password) is not None

    return isLongEnough and hasUpper and hasLower and hasDigit


password = '123456aA'
print(isStrongPassword(password))

