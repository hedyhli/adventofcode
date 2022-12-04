import re

from aocd import submit

with open("input.txt") as f:
    lines = [ list(map(int, re.split(",|-", l))) for l in f.read().strip().split('\n') ]

# wtf?
n = len(list(filter(lambda l: (l[0]<=l[2]<=l[3]<=l[1] or l[2]<=l[0]<=l[1]<=l[3]), lines)))
print(n)
submit(n, year=2022, part="a", day=4)
n = len(list(filter(lambda l: (l[0]<=l[3]>=l[2]<=l[1]), lines)))
print(n)
submit(n, year=2022, part="b", day=4)

# old implementation
# n = len(list(filter(lambda l: (l[0] >= l[2] and l[1] <= l[3]) or (l[2] >= l[0] and l[3] <= l[1]), lines)))
# n = len(list(filter(lambda l: (len(set(range(l[0], l[1]+1)) & set(range(l[2], l[3]+1))) > 0), lines)))
