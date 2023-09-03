import random

def main():
        while True: # main game loop
            secreNum = getSecretNum()
            print('''Bages, a deductive logic game.
                  By Al Sweigart al@inventwithpython.com
                  
                  I am thinking of a {}-digit number with no repeated digits.
                  Try to guess what it is. Here are some clues:
                  When I say:   That means:
                    Pico  One digit is correct but in the wrong position.
                    Fermi One digit is correct and in the right position.
                    Bagels    No digit is correct.
                  
                  For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
                  '''.format(NUM_DIGITS)))
            print('I have thought up a number.')
            print(' You have {} guesses to get it.'.format(MAX_GUESSES))

            numGuesses = 1
            while numGuesses <= MAX_Guesses:
                  guess= ''