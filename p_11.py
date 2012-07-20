from operator import mul
#text file with grid written to it
with open("p_11.txt") as f:
    grid = [map(lambda x: int(x), line.strip().split()) for line in f]


def product_vert(row, pos):
    if row in xrange(17, 20):
        return 1
    else:
        return reduce(mul, [grid[x][pos] for x in xrange(row, row + 4)])


def product_hori(row, pos):
    if pos in xrange(0, 3):
        return 1
    else:
        return reduce(mul, [grid[row][x] for x in xrange(pos, pos - 4, -1)])


def product_diags(row, pos):
    if row in xrange(17, 20) or pos in xrange(17, 20):
        diag_down = 1
    else:
        diag_down = reduce(mul, [grid[row + x][pos + x] for x in xrange(4)])
    if row in xrange(0, 3) or pos in xrange(17, 20):
        diag_up = 1
    else:
        diag_up = reduce(mul, [grid[row - x][pos + x] for x in xrange(4)])
    return max(diag_up, diag_down)

max_tup_list = [(product_diags(x, y), product_hori(x, y), product_vert(x, y))
                 for x in xrange(20) for y in xrange(20)]
answer = max(max(max_tup_list))
print answer
