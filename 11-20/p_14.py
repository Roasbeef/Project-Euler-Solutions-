'''
Which starting number, under one million,
produces the longest chain?
'''

cache = {}


def len_collatz(starting_num):
    steps = 0
    current_num = starting_num
    while True:
        if current_num in cache:
            cache[starting_num] = steps + cache[current_num]
            return steps + cache[current_num]
        elif current_num == 1:
            break
        elif not current_num % 2:
            current_num = current_num / 2
        else:
            current_num = (3 * current_num) + 1
        steps += 1

    cache[starting_num] = steps + 1
    return steps + 1


answer = max(((len_collatz(x), x) for x in xrange(1, 1000001)))[1]

print answer  # 837799
