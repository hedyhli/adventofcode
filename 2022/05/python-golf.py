a,b=open(0).read().split('\n\n');c=[""]*9
for l in a.split('\n')[::-1]:
 for m in (r:=__import__('re').finditer)("(\w)",l):c[m.span()[0]//4]+=(m.groups()[0])
C=c.copy()
def F(c,x):
 for m in r("(\d+).*(\d+).*(\d+)",b):n,f,t=map(int,m.groups());f-=1;t-=1;l=len(c[f]);c[t]+=c[f][l-n:][::x];c[f]=c[f][:l-n]
 print("".join(i[-1] for i in c))
F(c,-1);F(C,1)

# 353
