import numpy
import itertools
import math
#choose n
n = 7
#create a random array of length n
ranvec = numpy.random.rand(n)
#store all the possible permutations in a list
per = list(itertools.permutations(ranvec))
#create a function to find the distance to the closest number to a fixed number in an array z
def smallest(z,y):
    a = 100000
    for i in range(0,y):
        w = z[i] - z[y]
        if abs(w) < a:
           a = abs(w)
    return a

#calculate the total number of "claps" in all the permutations
c = 0
x = math.factorial(n)
for i in range(0,x):
    b = 100000
    z = per[i]
    for j in range(1,n):
       if smallest(z,j) < b:
          c = c + 1
          b = smallest(z,j)
#divide the total number of claps by n! to calculate the expectation
exp = c/x
print(exp)
