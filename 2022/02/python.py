from aocd import submit


with open("input.txt") as f:
    lines = [ tuple(map(ord, list(line.strip()))) for line in f ]

score = sum((3,6,0)[(x-a)%20%3]+x-87 for a,_,x in lines)
print(score)
submit(score, part="a", year=2022, day=2)

# part 2
score = 0
for a,_,x in lines:
    score += x*3-264
    if x == 88:
        score += (2,0,1)[a-65]+1
    if x == 89:
        score += a-64
    if x == 90:
        score += (1,2,0)[a-65]+1

print(score)
submit(score, part="b", year=2022, day=2)


## HARDCODING IS RETARDED
## HARDCODING IS FOR THE WEAK!!!
