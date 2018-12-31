#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

# Input string
pyperclip.copy('''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars''')
text = pyperclip.paste()

lines = text.split('\n')
newLines = []
for line in lines:
    newLines.append('* ' + line)

newText = '\n'.join(newLines)
print(newText) # pyperclip.copy(newText)
