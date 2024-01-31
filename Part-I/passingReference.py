import copy

def eggs(someParameter):
    someParameter.append('Hi')

# using copy module
def listCopy(someParam):
    someParam.append('copy')

spam = [1,2,3]
eggs(spam)
print(spam)

listCopy(copy.copy(spam))
print(spam)

# deepcopy
deep_copy = [1,2,[4,5,6]]
listCopy(copy.deepcopy(spam))
print(deep_copy)