D=(1,-1j,-1,1j)
print(*[(c:=0)+(p:=0)+1+int(sum((((c:=c+m).real-p.real)*(c.imag+p.imag)+abs(m)+0*(p:=c))/2for m in M).real)for M in zip(*((D['RDLU'.find(a)]*int(b),D[int(c[7])]*int(c[2:7],16))for a,b,c in map(str.split,open(0))))])
