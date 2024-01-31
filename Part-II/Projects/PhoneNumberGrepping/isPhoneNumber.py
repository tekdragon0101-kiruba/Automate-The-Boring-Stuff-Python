#! Python3 
# isPhoneNumber.py - Verify the text is phone number or not.

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' and text[7] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

def findPhoneNumber(message):
    isFound = False
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            isFound = True
            print('Phone number found: '+ chunk)
    if not isFound:
        print('Sorry, Phone number not found in this messages.')
    print('done')


# check the text is phone number or not.
print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

# check phone number is in messages or not.
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
findPhoneNumber(message)
findPhoneNumber('Hi I am kirubakaran, I will become a ethical hacker and bug bounty hunter. 75843-8qu90')