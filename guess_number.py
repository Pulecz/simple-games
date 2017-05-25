#!/usr/bin/env python

import random

#settings
max_number=10
guesses = 3
debug=False

def guess_number(guesses = 3, debug = False):
    "main game logic"

    def handle_input():
        "return only int and number in bounds"
        user_input = input('Guess a number from 0 to ' + str(max_number) + ':\n')
        try:
            int(user_input)
        except ValueError:
            print('Please insert by only a number\nTry again')
            handle_input()
        #can convert to int, now save the variable
        users_number = int(user_input)
        if users_number < 0 or users_number > max_number:
            print('Number', users_number, 'is out of bounds\nTry again')
            handle_input()
        else:
            return users_number

    def evaluate(target, users_guess, guesses):
        'evaluate if user is correct'
        if users_guess == target:
            print('You got it!')
            return True
        else:
            if guesses != 1: #has to be, so 3 guesses are really 3, not 4
                print('Wrong, try again')
                guesses -= 1
                users_guess = handle_input()
                evaluate(target, users_guess, guesses)
            else:
                print('Out of tries, you lost')
                return False


    #generate number
    target = random.randint(0,max_number)
    if debug: print(target)
    #take input
    users_guess = handle_input()
    #let user guess until guesses run out
    evaluate(target, users_guess, guesses)

if __name__ == '__main__':
    guess_number(guesses = guesses, debug=debug)
