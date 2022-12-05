import re
from aocd import submit

with open("input.txt")as f:
    a, b = f.read().split('\n\n')

c = [""]*9
for l in a.splitlines()[::-1]:
    for m in re.finditer("\[(\w)\]", l):
        c[m.span()[0]//4] += (m.groups()[0])

C = [i for i in c]

for m in re.finditer("(\d+) \w+ (\d+) \w+ (\d+)", b):
    n, f, t = map(int, m.groups())
    f-=1; t-=1; l = len(c[f])
    c[t] += c[f][l-n:][::-1];  c[f] = c[f][:l-n]
    C[t] += C[f][l-n:];        C[f] = C[f][:l-n]

print(m := "".join(i[-1] for i in c))
submit(m, year=2022, day=5, part="a")
print(m := "".join(i[-1] for i in C))
submit(m, year=2022, day=5, part="b")



# old impl
# for m in d.finditer(inp[s]):
#     col = m.span()[1]-1
#     crates.append("")
#     for l in inp[:s+1]:
#         if l[col].isalpha():
#             crates[-1] += l[col]
#     crates[-1] = list(reversed(crates[-1]))
#
# for m in op.finditer("\n".join(inp[10:])):
#     n, fr, to = (tuple(map(int, m.groups())))
#     fr -= 1; to -= 1
#     l = len(crates[fr])
#     crates[to].extend(reversed(crates[fr][l-n:]))
#     crates[fr] = crates[fr][:l-n]
#     # print(crates[fr][:l-n])
# m = "".join(i[-1] for i in crates)
# submit(m, year=2022, day=5, part="a")
