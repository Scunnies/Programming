#prompts the user to guess a number
# program keeps prompting the user 
# until the user guesses correct number
#Author: Eleanor Sammon

GuessNumber = 26


# as long as the input doesn't match the target number
# it will return "Wrong!"
guess = int (input ("Guess a number between 1 and 30: "))
while guess != GuessNumber:
    print ("Wrong!")
    guess = int (input ("Guess again: "))

# this will output only when input matches the GuessNumber
# and therefore ends the while loop
print ("Well done!")
