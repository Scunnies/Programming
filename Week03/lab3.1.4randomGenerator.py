#lab 3.4
#this program prints a random number between 1 and 10
#author: Eleanor Sammon

#we need the module random
import random

# establish two variables and convert to integers
firstNo = int(input("choose the first number in your range: "))
secNo = int(input("now choose a second, higher, number: "))

#formula to randomise the result from the two variables given
number = random.randint(firstNo,secNo)

#print the output
print ("this is a random number within your range: {} " .format(number))