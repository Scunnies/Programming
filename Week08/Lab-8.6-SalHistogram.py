# histogram of salaries from lab 8.1
# Author: Eleanor Sammon

import numpy as np
import matplotlib.pyplot as plt


minSalary = 20000
maxSalary = 80000
numberOfEntries = 100


np.random.seed(1) # so the random numbers are the same each time program runs

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
# print (salaries) I just did this to see what numbers were being used!

plt.hist(salaries)
plt.show()