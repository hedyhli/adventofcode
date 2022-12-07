# goal: short but not golfed

from aocd import submit


with open("input.txt") as f:
    lines = f.read().strip().split("\n")

p = []
d = {}

for l in lines:
    if l.endswith(".."):
        p.pop()
    elif l.startswith("$ cd"):
        a = l[5:]
        p.append(a)
        if (key:="/".join(p)) not in d.keys():
            d[key] = 0
        continue
    elif l[0].isdigit():
        a = int(l.split(" ")[0])
        for j in range(1, len(p)+1):
            d["/".join(p[:j])] += int(a)


print(s:=sum(i for i in d.values() if i <= 1e5))
submit(s, part="a", day=7, year=2022)

want = 3e7  - 7e7 + d["/"]
print(s:=sorted(s for s in d.values() if s >= want)[0])
submit(s, part="b", day=7, year=2022)
