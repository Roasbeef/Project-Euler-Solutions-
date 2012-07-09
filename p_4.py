'''a
Find the largest palindrome
made from the product of two
3-digit numbers
'''

is_palindrome = lambda x: str(x) == str(x)[::-1]
number_range = (y * x for x in xrange(100, 999) for y in xrange(x, 999))
answer = max(filter(is_palindrome, number_range))  # 906609

print answer
