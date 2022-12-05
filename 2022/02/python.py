from aocd import submit


with open("input.txt") as f:
    lines = [ list(map(ord, list(line.strip()))) for line in f ]

score = sum((3,6,0)[(r[2]-r[0])%20%3]+r[2]-87 for r in lines)
print(score)
submit(score, part="a", year=2022, day=2)

# part 2
score = 0
for r in lines:
    score += r[2]*3-264
    if r[2] == 88:
        score += (2,0,1)[r[0]-65]+1
    if r[2] == 89:
        score += r[0]-64
    if r[2] == 90:
        score += (1,2,0)[r[0]-65]+1

print(score)
submit(score, part="b", year=2022, day=2)


## HARDCODING IS RETARDED
## HARDCODING IS FOR THE WEAK!!!
