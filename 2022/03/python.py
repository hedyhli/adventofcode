import string
from more_itertools import grouper

from aocd import submit

letters = string.ascii_letters


with open("input.txt") as f:
    lines = [ i.strip() for i in f.readlines() ]


priorities = 0
for line in lines:
    half = len(line) // 2
    both = set(line[:half]) & set(line[half:])
    for char in both:
        priorities += letters.find(char) + 1
    # print(both, priorities)

# print(priorities)
submit(priorities, year=2022, day=3, part="a")


priorities = 0
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

# using more-itertools
for l1, l2, l3 in grouper(lines, 3):
    priorities += letters.find( (set(l1) & set(l2) & set(l3)).pop()) + 1

submit(priorities, year=2022, day=3, part="b")
