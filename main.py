import re
import numpy
import math

#Function F(x) given in the task
def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

#We create an NxN coefficient matrix
m = numpy.zeros(shape=(2,2))
v = []
x = [1, 15]
        
for i in range(2):    
    for j in range(2):        
        m[i][j] = 1.0 * (x[i] ** j) # Our linear equation looks like a_j * x_i ^ j
    v.append(f(x[i]))
    
print(numpy.linalg.solve(m, v))

#Two
m = numpy.zeros(shape=(3,3))
v = []
x = [1, 8, 15]
        
for i in range(3):    
    for j in range(3):        
        m[i][j] = 1.0 * (x[i] ** j)         
    v.append(f(x[i]))
print(numpy.linalg.solve(m, v))    

#Three    
m = numpy.zeros(shape=(4,4))
v = []
x = [1, 4, 10, 15]
        
for i in range(4):    
    for j in range(4):
        #print(i, j)
        m[i][j] = 1.0 * (x[i] ** j) 
        #print(x[i], j)
    v.append(f(x[i]))
        
print(numpy.linalg.solve(m, v))