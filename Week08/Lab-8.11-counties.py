# pie plot of unique occurences of values in an array of county names
# Author: Eleanor Sammon


import numpy as np
import matplotlib.pyplot as plt


# make the array of occurences
possibleCounties = ['Clare', 'Limerick', 'Galway', 'Sligo','Mayo']
# pick 100 randomly from possible counties with the frequency set out in p


counties = np.random.choice(
possibleCounties,
p=[0.1, 0.3, 0.2, 0.12, 0.28], # probabilities have to sum to 1
size=(100)
)
# number of occurences of each county
# returns a tuple of the unique values and how many times they appear
unique, counts = np.unique(counties, return_counts = True)


plt.pie(counts, labels= unique)
plt.show()
