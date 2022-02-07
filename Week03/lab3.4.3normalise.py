# this program reads in a string, strips any leading/trailing spaces,
# converts string to lower case and outputs the length of input and output strings
#Author: Eleanor Sammon

#note, the strip function did not work when I used it so I found a different way using replace
rawString = input("Please enter a string:\t")
normalisedString = rawString .replace(" ", "") .lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print("That String normalised is: {}" .format(normalisedString))
print("We reduced the length of the string from {} to {}" .format(lengthOfRawString, lengthOfNormalised))