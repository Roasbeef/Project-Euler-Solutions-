'''
There exists exactly one Pythagorean triplet
for which a + b + c = 1000.
Find the product abc.
'''

answer = [(a * b * c) for c in xrange(505, 0, -1)
                      for a in xrange(c, 0, -1)
                      for b in xrange(a, 0, -1)
                      if a + b + c == 1000
                      and a ** 2 + b ** 2 == c ** 2][0]

print answer
