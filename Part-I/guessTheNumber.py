import random

# constants
LOW = 1
HIGH = 20
no_of_guesses = 0

def printHint(user_number):
    if numberToGuess > user_number:
        print('your guess is too low.')
    else:
        print('your guess is too high')
        
if __name__ == '__main__':
    numberToGuess = random.randint(LOW, HIGH)
    user_number = 0
    print(f"I am thinking of the number between {LOW} and {HIGH}.")
    while numberToGuess != user_number and no_of_guesses < 4:
        print("Take the guess.")
        try:
            user_number = int(input())
            no_of_guesses += 1
            if user_number != numberToGuess:
                printHint(user_number)
            continue
        except ValueError:
            print('You enter value is not number.')
    if user_number == numberToGuess:
        print(f'Good job! You guessed my number in {no_of_guesses} guesses!')
    else:
        print(f"You're crossed limit to guess, the correct number is {numberToGuess}.")