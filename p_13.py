"""
Work out the first ten digits of
the sum of the following one-hundred
50-digit numbers
"""

#numbers in text file
with open("p_13.txt") as f:
    result = str(sum([int(line) for line in f.readlines()]))[:10]
    print result  # '5537376230'
