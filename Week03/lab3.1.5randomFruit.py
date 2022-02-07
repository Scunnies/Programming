#lab 3.5
# this program prints a random fruit from a list
#author: Eleanor Sammon

#import the module for random
import random

#establish the variables
fruit = ["pear", "raspberry", "banana", "apple"]

#instruction to randomise the selection
index = random.randint(0, len(fruit)-1)
fruit = fruit[index]

#print the result
print ("a random fruit is: {}" .format(fruit))