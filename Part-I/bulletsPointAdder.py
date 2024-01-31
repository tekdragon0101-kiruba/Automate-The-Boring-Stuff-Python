#! Python3
# bulletPointAdder.py - Adds bullets to text in clipboard.
# copied bullets added contents to clipboard. 

import pyperclip

text = pyperclip.paste() # clipboard to variable
# my code 
def myCode(bulletDesign):
    bulletPoints = '\n' + bulletDesign + ' '
    pyperclip.copy(bulletDesign :+ ' ' + text.replace('\n', bulletPoints))

# book code
def bookCode():
    global text
    lines = text.split('\n')
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i] # add star to each string in 'lines'
    text = "\n".join(lines)
    pyperclip.copy(text)


bulletDesign = input('Enter your bullet point design (Enter to default *): ')
if bulletDesign == '':
    bookCode()
else:
    myCode(bulletDesign)

# Result verification
print(pyperclip.paste())