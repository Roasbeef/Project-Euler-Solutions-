'''
Which starting number, under one million,
produces the longest chain?
'''


def len_collatz(num):
    seq = [num]
    while seq[-1] > 1:
        if not seq[-1] % 2:
            seq.append(seq[-1] / 2)
        else:
            seq.append((3 * seq[-1]) + 1)
    return len(seq), num

answer = max([len_collatz(x) for x in xrange(1000001)])[1]

print answer  # 837799
