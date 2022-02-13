# reads in a students percentage mark and
# prints out corresponding grade
#Author: Eleanor Sammon

# ask user to input their % grade
percentage = float (input ("Enter your grade: "))

# set out the parameters for how the program
# should output depending on the grade

if percentage <1 or percentage >100:
    print ("Please print a number between 1 and 100")
elif percentage <40: #no need to set a lower parameter as it has to be greater than 1
    print ("Fail")
elif percentage <50: # captures data between 40 and 50
    print ("Pass")
elif percentage <60: # captures data between 50 and 60
    print ("Merit1")
elif percentage <70: # captures data between 60 and 70
    print ("Merit2")
else: # captures all remaining results between 70 and 100
    print ("Distinction")