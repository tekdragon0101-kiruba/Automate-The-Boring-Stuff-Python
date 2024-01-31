#! python3 
# passwordDetection.py - validate the strength of the password.

import re

passwordPattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?_&]{8,}$', re.MULTILINE)

# Get the user input 
password = input('Enter your password to check the Strength: ')
if passwordPattern.match(password):
    print('Your password strength is Strong.')
else:
    print('Your password strength is Weak.')