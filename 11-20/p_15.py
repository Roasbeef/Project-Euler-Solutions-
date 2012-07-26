'''
Starting in the top left corner in a
20 by 20 grid, how many routes
are there to the bottom right corner?
'''
from operator import mul
answer = reduce(mul, range(21, 41)) / reduce(mul, range(2, 21))
print answer
