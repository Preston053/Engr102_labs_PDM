# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Preston Montgomery
# Section:      522
# Assignment:   Lab 112-1
# Date:         11 12 2023

import numpy as np
import matplotlib.pyplot as plt

# begin with point (0, 1)
v = np.array([0,1])
# matrix: [ 1.02 0.095 / −0.095 1.02 ]
m = np.array([(1.012, 0.095),(-0.095, 1.02)])
points = np.array([])
# repeat for a total of 250 times.
fig, ax = plt.subplots()
for i in range(251):
    # multiply the matrix by the point to get a new point 
    v = m.dot(v)
    ax.plot(v[0], v[1], color='red', marker='h')
# label the x and y axes, include a title (shape of graph).
ax.set(xlabel='x', ylabel = 'y', title='My Confidence')
ax.grid()
plt.show()