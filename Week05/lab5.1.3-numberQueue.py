# a program that puts 10 random numbers into a queue/list, 
# outputs all the values in the queue
# takes the numbers from the queue one at a time
# prints that number and remaining numbers in the queue
# Author: Eleanor Sammon


import random

queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))
    print ("queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("the queue is now empty")