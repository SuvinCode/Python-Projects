# import the required libraries
import random
import matplotlib.pyplot as plt

# store the random numbers in a
# list
nums = [ ]
mu = 0
sigma = 0.25

for i in range(100):
    temp = random.lognormvariate(mu, sigma)
    nums.append(temp)

# plotting a graph
plt.plot(nums)
plt.show()