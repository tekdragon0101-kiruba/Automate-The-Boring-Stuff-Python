#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# This program for finding all phone numbers and email
# search in any text based contents like webpages, paragraph etc...

import pyperclip 
import re        

def matchPhoneNumbers(content):
    phoneRegex = re.compile(r'''
            (\d{3}|\(\d{3}\)) # area code
                            
                            ''', re.VERBOSE)


def matchEmails(content):
    pass


def help():
    pass


if __name__ == '__main__':
    # Get the clipboard content and store into Variable
    text = pyperclip.paste()
    