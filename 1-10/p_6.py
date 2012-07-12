'''
Find the difference between the sum of the squares
of the first one hundred natural numbers
and the square of the sum.
'''

answer = sum([x for x in xrange(1, 101)]) ** 2 - sum([x * x for x in xrange(1, 101)])
