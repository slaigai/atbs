#! python3
# pw.py - An insecure password locker program.

# The command line arguments will be stored in the variable sys.argv. (See Appendix B for more information on how to use
# command line arguments in your programs.) The first item in the sys.argv list should always be a string containing the
# program’s filename ('pw.py'), and the second item should be the first command line argument. For this program, this
# argument is the name of the account whose password you want. Since the command line argument is mandatory, you display
# a usage message to the user if they forget to add it (that is, if the sys.argv list has fewer than two values in it).
# Make your program look like the following:


import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)



