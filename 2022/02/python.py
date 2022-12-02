from aocd import submit


with open("input.txt") as f:
    lines = f.readlines()


shape = {
    'A': 1,
    'B': 2,
    'C': 3,
}

m = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

# how to win
win = {
    'C': 'A',
    'A': 'B',
    'B': 'C',
}
#...and how to lose
lose = {
    'C': 'B',
    'A': 'C',
    'B': 'A',
}

score = 0
for r in lines:
    if m[r[2]] == r[0]:
        score += 3
    if win[r[0]] == m[r[2]]:
        score += 6
    score += shape[m[r[2]]]

print(score)
submit(score, part="a", year=2022, day=2)

# part 2
score = 0
pts = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}
for r in lines:
    score += pts[r[2]]

    if r[2] == 'Y':
        score += shape[r[0]]
    if r[2] == 'Z':
        score += shape[win[r[0]]]
    if r[2] == 'X':
        # lose
        score += shape[lose[r[0]]]

print(score)
submit(score, part="b", year=2022, day=2)
