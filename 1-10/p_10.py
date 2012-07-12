# Find the sum of all the primes below two million.
import math


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True

answer = sum(filter(is_prime, xrange(2000000)))
