birthdays = {'aravind d': "1st Oct", 'naveen n': "5th Sep", 'chandru': '23rd Apr'}

while True:
    # getting input from user
    print("Enter a name (blank to quit): ")
    name = input().lower()
    if name == '':
        break
    if name in birthdays:
        print( birthdays[name] + " is the birthday of " + name.capitalize() + ".")
    else:
        print('I do not have the birthday information for '+ name.capitalize())
        print('What is their birthday date')
        bday = input().lower()
        birthdays[name] = bday
        print('Birthday Database updated.')