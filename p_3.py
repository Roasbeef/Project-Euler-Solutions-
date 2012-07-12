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

answer = max(prime_factors(600851475143))
