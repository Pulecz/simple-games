#!/usr/bin/env python
"""
Generate random number from 1 to max_number
Ask user for input
    validate if its a number (floats are ignored)
Compare generated number with user_input
"""
import random #for randint
from string import digits as numbers_for_humans #for showing user what strings are allowed

#settings
debug = False
max_number = 9
max_available_guesses = 3

def compare(user_input):
    """simply compare if the user_input is same value as target_number
    return True if values are equal, otherwise False
    """
    #target_number is global var
    if target_number == user_input:
        print('You guessed it!')
        return True
    else:
        print('Incorrect.')
        return False

if __name__ == '__main__':
    #working global var
    guesses = 0

    def ask_for_digit(limit=99):
        """Ask user for a whole number(int) and follow these rules:
           * positive int (using isdigit func) - note that any input with prefix '-' is not taken as a digit
           * no higher then max_number
        default limit is 99 KeyboardInterrupt handled

        only outcome is:
            * return of int following the rules
            * KeyboardInterrupt causing exit()
        '"""

        global guesses
        print('{} guesses left'.format(max_available_guesses - guesses))

        for chance in range(limit):
            #do input
            try:
                user_input = input('Guess a number from 1 to {}: '.format(max_number))
            except KeyboardInterrupt:
                print('Giving up? Boo')
                exit(1001)

            #got input in user_input which is str
            #if its a digit (hence no str) set repeat o
            ##if user_input.isdigit() and int(user_input) <= max_number:
            if user_input.isdigit(): #first condition
                if int(user_input) > max_number:
                    print('Please input number from 1 to 9')
                elif int(user_input) <= max_number: #second condition
                    break

            if chance >= 4: #if its already 5th wasted chance, print help
                print('Come on enter some number already!\nNumber is these characters {}'.format(
                    ' or '.join(n for n in numbers_for_humans))) #convert string to a list then list to a string

        user_input = int(user_input)
        guesses += 1
        return user_input

    #generate number
    target_number = random.randint(1, max_number)
    #if debug is on (True) show what the target_number is
    if debug: print(target_number)

    #game loop
    while True: #while user can make guess(es)
        user_input = ask_for_digit() #input is in this function, that is the 'pause' in while loop
        if compare(user_input):
            #user won, exit
            exit(0) #win
        else:
            #user didn't get it, ask for new input again
            pass
        #check if guesses are exhausted
        if guesses == max_available_guesses:
            #all guesses exhausted
            print('The target number was', target_number,'\nBetter luck next time!')
            exit(1) #lose

