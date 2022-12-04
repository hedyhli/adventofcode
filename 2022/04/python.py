from aocd import submit

with open("input.txt") as f:
    lines = f.read().strip().split('\n')


n = 0
for line in lines:
    a, b = line.split(',')
    a1, a2 = (int(i) for i in a.split('-'))
    b1, b2 = (int(i) for i in b.split('-'))
    if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
        n += 1
        # print(line, a1, a2, b1, b2)

print(n)
submit(n, year=2022, part="a", day=4)

n = 0
for line in lines:
    a, b = line.split(',')
    a1, a2 = (int(i) for i in a.split('-'))
    aset = set(range(a1, a2+1))
    b1, b2 = (int(i) for i in b.split('-'))
    bset = set(range(b1, b2+1))
    if len(aset & bset) > 0:
        n += 1
        # print(line)

print(n)
submit(n, year=2022, part="b", day=4)
