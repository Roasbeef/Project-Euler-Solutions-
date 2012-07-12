#Sum of even numbers of the fib sequence uner 4,000,000


def fibs_under(n):
    fibs = [0, 1]

    while fibs[-1] < n:
        fibs.append(sum(fibs[-2:]))
        if fibs[-1] > n:
            #went over so remove last
            return fibs[:-1]
    return fibs

answer = sum(filter(lambda x: x % 2 == 0, fibs_under(4000000)))
