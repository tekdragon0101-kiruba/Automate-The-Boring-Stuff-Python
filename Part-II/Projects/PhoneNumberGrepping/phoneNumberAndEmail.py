#! python3
# phoneNumberAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip, re

# Global variabes
global extractedContent 
extractedContent = str()


# Function for Check the Phone Number Pattern
def checkPhoneNumbersForIndia(text):
    phoneNumberPattern = re.compile(r'''
(?:\+91)?0?[\s\-]? # for +91 and space 
(\d{5}[\s\-]?\d{5}| # for 5 + 5 phone numbers eg. 64578 96534
\d{3}[\s\-]?\d{3}[\s\-]?\d{4}) # for 3 + 3 + 4 phone numbers 
# eg. 645 789 6534 OR 645-789-6534
''', re.VERBOSE)
    return phoneNumberFormatter(phoneNumberPattern.findall(text))

# Change Phone numbers in unique Format
def phoneNumberFormatter(phoneNumbers):
    results = list()
    if phoneNumbers:
        for n in phoneNumbers:
            if '-' in n:
                n = n.replace('-','')
            elif ' ' in n:
                n = n.replace(' ','')
            results.append(re.sub(r'(\d{3})(\d{3})(\d{4})',r'\1-\2-\3',n))
    return results

# Function for Check email addresses
def checkEmailAddress(text):
    mailAddressPattern = re.compile(r'''
[a-z0-9\-\_\.\%\+]+ # abcd_12344
@[a-z]+ # @gmail OR @yahoo
\.[a-z]{2,4} # .com 
''',re.VERBOSE )
    return mailAddressPattern.findall(text)

# Formatting the Output 
def ListsFormatter(lists):
    global extractedContent
    if lists:
        for element in lists:
            extractedContent += element + '\n'
        

if __name__ == '__main__':
    text = str(pyperclip.paste())
    phoneNumbersList = checkPhoneNumbersForIndia(text)
    emailsList = checkEmailAddress(text)
    ListsFormatter(phoneNumbersList)
    ListsFormatter(emailsList)

    # Copy results to clipboard
    if extractedContent != '':
        pyperclip.copy(extractedContent)
        print('Copied to clipboard')
        print(extractedContent)
    else:
        print('No phone numbers or email addresses found.')