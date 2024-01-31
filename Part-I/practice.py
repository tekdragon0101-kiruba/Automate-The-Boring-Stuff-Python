spam = {'cat': 'meow..'}
if 'cat' in spam:
    print(True)
    
if 'cat' in spam.keys():
    print(True)
if 'cat' in spam.values():
    print(True)
else:
    print(False)

spam.setdefault('color','black')
print(spam)