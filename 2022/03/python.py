from string import ascii_letters as letters; letters = " "+letters

from more_itertools import grouper
from aocd import submit

with open("input.txt") as f:
    lines = f.read().strip().split('\n')

# part 1
priorities = sum(letters.find((set(l[:len(l)//2]) & set(l[len(l)//2:])).pop()) for l in lines)
submit(priorities, year=2022, day=3, part="a")
# part 2
priorities = sum(letters.find((set(l1) & set(l2) & set(l3)).pop()) for l1, l2, l3 in grouper(lines, 3))
submit(priorities, year=2022, day=3, part="b")


# old implementations
# part 2
# items = []
# for line in lines:
#     line = line.strip()
#     items.append(set(line))
#     if len(items) == 3:
#         # group
#         common = items[0] & items[1] & items[2]
#         for char in common:
#             priorities += letters.find(char) + 1
#             # print(common, priorities)
#         items = []
