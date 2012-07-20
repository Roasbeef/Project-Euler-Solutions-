"""
What is the value of the first triangle number
to have over five hundred divisors?
"""
import itertools


#def factors(n):
#    return [i for i in xrange(1, n // 2 + 1) if not n % i] + [n]
def factors(n):
    a, r = 1, [1]
    while a * a < n:
        a += 1
        if n % a:
            continue
        b, f = 1, []
        while n % a == 0:
            n //= a
            b *= a
            f += [i * b for i in r]
        r += f
    if n > 1:
        r += [i * n for i in r]
    return r


def tri_num(n):
    return sum(range(n + 1))


def tri_fac_gen():
    n = 1
    while True:
        yield (tri_num(n), len(factors(tri_num(n))) - 1)
        n += 1

answer = list(itertools.takewhile(lambda x: x[1] < 580, tri_fac_gen()))

print max(answer, key=lambda x: x[1])  # 76576500
