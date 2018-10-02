import re
import numpy
import math
from matplotlib import pyplot as plt

#Function F(x) given in the task
def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
#We create a NxN coefficient matrix need in order to solve the system of linear equations
def createMatrix(x):
    n = len(x)
    matrix = numpy.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = x[i] ** j
    return matrix
#Create the array of points(f(x[i]), where x[i] ranges from 1 to 15, with a step of 1) on which we will build out function
def createFunc(rank, scope):
    y = numpy.zeros(shape=(len(scope)))
    for i in range(len(scope)):
        for j in range(len(rank)):
                y[i] += rank[j] * (scope[i] ** j)
    return y

scope = numpy.arange(1, 15, .1)
x2 = [1, 15]
m2 = createMatrix(x2)    
v2 = list(map(f, x2))
a2 = numpy.linalg.solve(m2, v2)

x3 = [1, 8, 15]
m3 = createMatrix(x3)    
v3 = list(map(f, x3))
a3 = numpy.linalg.solve(m3, v3)

x4 = [1, 4, 10, 15]
m4 = createMatrix(x4)    
v4 = list(map(f, x4))
a4 = numpy.linalg.solve(m4, v4)
                    
y = list(map(f, scope))
y2 = createFunc(a2, scope)
y3 = createFunc(a3, scope)
y4 = createFunc(a4, scope)
plt.plot(scope, y)
plt.plot(scope, y2)
plt.plot(scope, y3)
plt.plot(scope, y4)
plt.show()