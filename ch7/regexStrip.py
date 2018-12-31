# Regex Version of strip()

# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are
# passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the
# string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

import re


def regexStrip(s, strRm=None):
    if strRm is None:
        strRep = r'^\s*|\s*$'
    else:
        strRep = strRm

    return re.sub(strRep, '', s)


print(regexStrip('    abc    '))
print(regexStrip('    abc    ', 'b'))





