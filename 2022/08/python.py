from aocd import submit

with open(0) as f:
    lines = [tuple(map(int, line)) for line in f.read().strip().splitlines()]


def viewdist(current: int, view: list, reverse=False):
    n = 0
    iterator = view
    if reverse:
        iterator = reversed(iterator)
    for i in iterator:
        if current > i:
            n += 1
        elif current <= i:
            n += 1
            break
    return n


# Part 1
n = len(lines)*2 + (len(lines[0])-2)*2  # Edges
# Part 1
max_score = 0

for i in range(1, len(lines)-1):
    row = lines[i]
    for j in range(1, len(row)-1):
        left    = row[:j]
        right   = row[j+1:]
        top     = [ l[j] for l in lines[:i] ]
        bottom  = [ l[j] for l in lines[i+1:] ]

        current = row[j]
        # Part 1
        if (current > max(left) or current > max(right) or
            current > max(top) or current > max(bottom)):
            n += 1
        # Part 2
        score = 1
        for view in left, top:
            vd = viewdist(current, view, reverse=True)
            score *= vd
        for view in right, bottom:
            vd = viewdist(current, view, reverse=False)
            score *= vd
        if score > max_score:
            max_score = score

print(n)
submit(n, "a", 8, 2022)
print(max_score)
submit(max_score, "b", 8, 2022)
