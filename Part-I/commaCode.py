import copy

def convertStringWithCommas(listValue):
    sentence = str()
    for i in range(len(listValue)):
        if i < len(listValue) - 1:
            sentence += str(listValue[i]) + ', ' 
        else:
            sentence += 'and ' + str(listValue[i])
    return sentence

if __name__ == '__main__':
    # pets_list = ['dogs','cats','parrots','cows']
    numbers = [ i for i in range(int(input()))]
    arg = copy.copy(numbers)
    print(arg)
    results = convertStringWithCommas(arg)
    print(results)
    print(type(results))