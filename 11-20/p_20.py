from operator import mul

answer = sum(map(lambda x: int(x), str(reduce(mul, range(1, 101)))))
print answer  # 648
