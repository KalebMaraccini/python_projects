import random

def main():
      print('''Bages, a deductive logic game.
                  By Al Sweigart al@inventwithpython.com
                  
                  I am thinking of a {}-digit number with no repeated digits.
                  Try to guess what it is. Here are some clues:
                  When I say:   That means:
                    Pico  One digit is correct but in the wrong position.
                    Fermi One digit is correct and in the right position.
                    Bagels    No digit is correct.
                  
                  For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
                  '''.format(NUM_DIGITS))
      while True: # main game loop
            # store the secret number the player has to guess
            secretNum = getSecretNum() 
            print('I have thought up a number.')
            print(' You have {} guesses to get it.'.format(MAX_GUESSES))

            numGuesses = 1
            while numGuesses <= MAX_Guesses:
                  guess= ''
                  # loop until user enters a valid number
                  while len(guess) != NUM_DIGITS or not guess.isdecimal():
                        print('Guess #{}: '.format(numGuesses))
                        guess = input('> ')

                        clues = getClues(guess, secretNum)
                        print(clues)
                        numGuesses += 1

                        if guess == secretNum:
                              print('You got it!')
                              break # they're correct, break loop
                        if numGuesses > MAX_Guesses:
                              print('You ran out of guesses.')
                              print('The answer was {}.'.format(secretNum))
            # ask user if they want to play again
            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                  break
      print('Thanks for playing!')

def getSecretNum():
      #Returns a string made up of NUM_DIGITS unique random digits
      