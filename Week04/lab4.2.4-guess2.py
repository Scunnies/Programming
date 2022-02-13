#prompts the user to guess a number
# program keeps prompting the user 
# until the user guesses correct number
#Author: Eleanor Sammon


# for the second element of this lab
# I googled and found the answer at 
# https://www.programiz.com/python-programming/examples/random-number

import random
GuessNumber = (random.randint(0,100))


# as long as the input doesn't match the target number
# it will return "Wrong!"
guess = int (input ("Guess a number between 1 and 100: "))
while guess != GuessNumber:
    if guess < GuessNumber:
        print ("Too low!")
    else:
        print ("Too high!")
    guess = int (input ("Guess again: "))

# this will output only when input matches the GuessNumber
# and therefore ends the while loop
print ("Well done!")
