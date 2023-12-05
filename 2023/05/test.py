from more_itertools import grouper

with open('input.txt') as f:
    line = [ int(i) for i in f.readline()[7:].strip().split() ]
    for a, n in grouper(line, 2):
        print(f"{a:-10}\n{a+n:-10}")
        print('---')
