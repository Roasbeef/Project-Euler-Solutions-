import math
# Find the 10,000st prime number


def prime_range():
    primes = []
    num = 3
    while len(primes) < 10000:
        if num % 2 == 0:
            num += 1
            continue
        elif is_prime(num):
            primes.append(num)
        num += 1
    return primes


def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(math.sqrt(num) + 1)):
        if num % x == 0:
            return False
    return True

answer = prime_range()[-1]
