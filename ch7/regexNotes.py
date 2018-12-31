# Notes on regex

import re

# Passing a string value representing your regular expression to re.compile() returns a Regex pattern object (or simply,
# a Regex object).
# Using a raw string to capture \d as a string and not an escaped d. A raw string does not escape characters
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Use the Regex object to search text
# mo variable name is just a generic name to use for Match objects
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

# Grouping with parentheses to return groups of text
# use the group() match object method to grab the matching text from just one group
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))  # 415
print(mo.group(2))  # 555-4242
print(mo.group(0))  # 415-555-4242 (returns the entire match)
print(mo.group())   # 415-555-4242 (returns the entire match)

areaCode, mainNumber = mo.groups() # Retrieve all groups at once using groups()
print('All groups', areaCode, mainNumber)  # ('415', '555-4242')

# Matching parentheses. Need to escape the parentheses
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))  # (415)

# Matching multiple groups with the pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

'''
You can find all matching occurrences with the findall() method that’s discussed in The findall() Method.
Returns all matches as a list as long as there are no groups in the regular expression

If there are groups in the regular expression, then findall() will return a list of tuples.
'''
moAll = heroRegex.findall('Batman and Tina Fey.')
print(moAll)

# Matching multiple suffixes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group(1)) # mobile
print(mo.group())  # Batmobile

# Match zero or one of the group with ?
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())  # Batman
print(mo2.group())  # Batwoman

# Match zero or more with *
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batwowowowoman')
print(mo1.group())  # Batwowowowoman

# Match one or more with +
# No need for example

# Match specific repetitions with curly braces
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHa')
print(mo1)  # None

# Greedy and nongreedy matching
# Python's regular expressions are greedy by default
#    They will match the longest string possible
# The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly
# bracket followed by a question mark
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())  # HaHaHa

# Character classes (e.g. \d, \s, \w)
xmasRegex = re.compile(r'\d+\s\w+')
xmasAll = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmasAll)  # ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

'''
Custom character classes
Note that inside the square brackets, the normal regular expression symbols are not interpreted as such

Make negative character classes by pusing ^ after closing bracket ]
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelAll = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowelAll)  # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantAll = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(consonantAll)  # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

'''
^ at start of regex to indicate match must occur at the beginning of the text
$ at start of regex to indicate match must occur at the end       of the text
'''
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('He said hello.')
print(mo)  # None

'''
The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline
'''
atRegex = re.compile(r'.at')
atAll = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atAll)  # ['cat', 'hat', 'sat', 'lat', 'mat']

'''
Match everything with .*
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))  # Al
print(mo.group(2))  # Sweigart

'''
match newlines with re.DOTALL as second arg to re.compile()
'''
newlineRegex = re.compile('.*', re.DOTALL)
newlineGroup = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
print(newlineGroup)


'''
To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile()
'''

'''
Substituting Strings with the sub() Method
'''
namesRegex = re.compile(r'Agent \w+')
namesSub = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(namesSub)  # CENSORED gave the secret documents to CENSORED.


'''
Mega regex management

You can mitigate this by telling the re.compile() function to ignore whitespace and comments inside the regular
expression string. This “verbose mode” can be enabled by passing the variable re.VERBOSE as the second argument to
re.compile()
'''
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)



