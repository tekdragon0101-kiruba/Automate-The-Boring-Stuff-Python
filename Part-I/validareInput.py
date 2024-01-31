while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number for your age: ')

while True:
    passwd = input('Select a new password (Letters and Numbers only): ')
    if passwd.isalnum():
        break
    print('Password can only have letters and numbers:')