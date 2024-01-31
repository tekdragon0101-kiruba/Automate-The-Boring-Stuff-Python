def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

if __name__ == "__main__":
    try:
        print('Enter Number: ')
        userNumber = int(input())
        while userNumber != 1 and userNumber != 0:
            userNumber = collatz(userNumber)
    except ValueError:
        print('You entered value is not number.')
