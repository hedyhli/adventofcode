s01 = lambda n: 1 if n != 0 else 0  # hmm (n//(n-1) or n//2 or 0) longer than this
m = lambda d: (0 if (y:=d%17) else 1)*1j*(x:=(1 if d%4 else -1)) + s01(y)*x  # move
t = lambda A, B: s01(A) * m(76 if A>0 else 82) + s01(B) * m(68 if B>0 else 85)  # keep up with prev knot, so they touch

with open("input.txt") as f:
    L = [ (ord(l[0]), int(l[2:])) for l in f.read().splitlines() ]

kn = [ 0 for _ in range(10) ]
v1 = set()  # part 1
vL = set()  # part 2

for d, a in L:
    for _ in range(a):
        kn[0] += m(d)
        for i in range(1, 10):
            kn[i] += 0 if (abs(A := (I := kn[i]).real-(I1 := kn[i-1]).real)<2) &\
                          (abs(B := I.imag-I1.imag)<2) else t(A, B)
        v1.add(kn[1])
        vL.add(kn[9])

print(s := len(v1))
print(s := len(vL))
