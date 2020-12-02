with open('inputs.txt') as f:
    li = [int(i.strip()) for i in f.readlines()]

from itertools import combinations

for com in combinations(li, 3):
    if sum(com) == 2020:
        print(com[0] * com[1] * com[2])
