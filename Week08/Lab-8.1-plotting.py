# this program manipulates and plots data about salaries
# Author: Eleanor Sammon

import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1) # to make sure my random numbers are the same each time

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000
salariesMult = salaries * 1.05
print (salariesMult)

newSalaries = salariesMult.astype(int)

