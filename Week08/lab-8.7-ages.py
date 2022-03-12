# plotting ages based off lab 8.1
# Author Eleanor Sammon

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100


np.random.seed(1)

salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 21, high = 65, size = numberOfEntries) 

plt.scatter(ages, salaries)
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints 

plt.plot(xpoints, ypoints, color='r', label = "X Squared")

plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("Age")

plt.legend()
plt.show() 

plt.savefig('prettier-plot.png')