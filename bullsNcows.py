#!/usr/bin/env python
bull_population = 4

from random import randint


def create_number(bulls):
    """Return random number in length of bulls"""
    result = ''
    for n in range(bulls):
        result += str(randint(0, 9))
    return result


def print_intro(bulls):
    print("""Welcome, let's play a game where you have to guess a number. \
People call it bulls and cows. You will have a chance to win {0} bulls, \
which you will get for each correctly guessed number. For each incorrect \
guess you will get a cow. And you will sure need those to get sucessfull \
herd.""".format(bulls)
)


def ask_user(bulls):
    """Ask user for input in length of the bulls."""
    the_guess = input("Guess {0} numbers: ".format(bulls))
    if len(the_guess) < bulls:
        print("You guessed only {0} numbers. Try again".format(len(the_guess)))
        ask_user(bulls)
    elif len(the_guess) > bulls:
        print("Too many numbers, taking only the first {0}".format(bulls))
        return the_guess[:bulls]
    else:
        return the_guess


def count_bulls_and_cows(guess, target):
    """
    Compares if two strings guess have same character on same position.
    In this case, for each same character, increase bulls
    and for each incorrect one, increase cows.
    """
    bulls = 0
    cows = 0
    for index, char in enumerate(str(guess)):
        if char in target[index]:
            bulls += 1
        else:
            cows += 1
    return (bulls, cows)


def evaluate_score(loops, total_cows):
    if loops == 0 and total_cows == 0:
        print("Congratulations. You guessed the number at first try!")
        print("Good luck maintaining your herd with no cows...")
    elif loops > 0 and loops <= 2 and total_cows < 3:
        print("Very good, you could use more cows though.")
    elif loops > 3 and loops <= 7 and total_cows <= 16:
        print("Impressive, just enough cows in less then five guesses.")
    elif loops > 3 and loops <= 7:
        print("Impressive. Quite a herd.")
    elif loops > 8:
        print("Nice guess. You were lucky.")
    elif loops > 16:
        print("You could do better.")
    else:
        print("Your performance needs no comments.")


def the_game(bull_population):
    loops = 1
    total_cows = 0
    print_intro(bull_population)
    the_number = create_number(bull_population)
    while True:
        player_guess = ask_user(bull_population)
        bulls, cows = count_bulls_and_cows(player_guess, the_number)
        if bulls == bull_population:
            total_cows += cows
            print("Correct, you got all the {0} bulls! It took you {1} guesses.\
 You also have {2} cows."
                  .format(bull_population, loops, total_cows))
            evaluate_score(loops, total_cows)
            exit(0)
        else:
            loops += 1
            total_cows += cows
            print("You have {0} bulls and {1} cows. Still need to get {2} bulls."
                  .format(bulls, cows, bull_population - bulls))

the_game(bull_population)
