############
# version 1#
############
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)

#fold list calculating lcm of each pair
result = reduce(lcm, range(2, 21))

#############
# version 2 #
#############
def prime_factors(n):
    factors = [1]
    last = n

    while last > 1:
        c = 2
        while last % c > 0:
            c += 1

        factors.append(c)
        last /= c
    return factors

#generate list of lcms of prime factorizations of 11-20
lcms = map(prime_factors, range(11, 21))
#remove 12 to avoid duplicates
lcms = lcms[:1] + lcms[2:]
#list of highest power of each prime factorization cutting off a repeat
lcms = sorted([max(x) ** x.count(max(x)) for x in lcms])[1:]
from operator import mul
#reduce list by multiplying
result = reduce(mul, lcms)
