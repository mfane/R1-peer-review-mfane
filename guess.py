#!/usr/bin/python3

import random
import sys

assert sys.version_info >= (3, 4), "This script requires at least Python 3.4"

# variables
guesses = 5
guess_range = 20
tries = 0
play = True
guess = 0

while play:
    # generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
    number = random.randint(1, guess_range)
    while tries < guesses:
        print("you have " + str(guesses - tries) + " tries left")
        # ask the user for a response and store it in the variable [guess]
        print("please put in a guess, from 1 to " + str(guess_range))
        guess = input()
        '''I separated these lines of code to avoid clutter and make it more clear where to type a response.'''

        # a try/except block is a great tool for programmers to be able to deal with errors.
        # In this instance, it reports an error if the user enters something other than an integer
        try:
            # convert the guess to an integer
            guess = int(guess)
            if guess < 1 or guess > 20:
                print("that number is not within the range")

            else:
                tries = tries + 1
                # check if the guess is less than the random number
                if guess < number:
                    print('Too low!')

                elif guess + 1 == number or guess - 1 == number:
                    print("you are very close!")

                elif guess == number:
                    print("yep, the number was " + str(number))
                    ask = True
                    tries = guesses
                    while ask:
                        print("do you want to play again? y/n")
                        answer = input()
                        '''Similar to the guesses, this will allow the input to be on a different line to make it more clear for the
                        Player where to put their response'''
                        if answer is "n" or answer is "N":
                            ask = False
                            play = False

                        elif answer is "y" or answer is "Y":
                            ask = False

                        else:
                            print("please only say y or n")

                else:
                    print("Too high!")

        except ValueError:
            print('Please only enter a whole number.')

    if number != guess:
        print("you ran out of guesses. the number was " + str(number))
        ask = True
        while ask:
            print("do you want to play again? y/n")
            answer = input()
            '''Similar to the guesses, this will allow the input to be on a different line to make it more clear for the
            Player where to put their response'''

            if answer is "n" or answer is "N":
                ask = False
                play = False

            elif answer is "y" or answer is "Y":
                ask = False

            else:
                print("please only say y or n")
    tries = 0
