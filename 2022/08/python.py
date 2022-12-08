with open(0) as f:
    L = [tuple(map(int, l)) for l in f.read().strip().splitlines()]

def vd(cur, v, rev=False):
    n = 0; it = v
    for i in (reversed(it) if rev else it):
        n += 1
        if cur <= i: break
    return n

n = len(L)*2 + (len(L[0])-2)*2
m = 0

for i in range(1, len(L)-1):
    row = L[i]
    for j in range(1, len(row)-1):
        cur = row[j]
        top = [ l[j] for l in L[:i] ]
        lef = row[:j]
        bot = [ l[j] for l in L[i+1:] ]
        rgt = row[j+1:]
        if (cur > max(lef) or cur > max(rgt) or
            cur > max(top) or cur > max(bot)):
            n += 1
        s = 1
        for v in lef, top:
            s *= vd(cur, v, True)
        for v in rgt, bot:
            s *= vd(cur, v, False)
        if s > m:
            m = s

print(n)
print(m)
