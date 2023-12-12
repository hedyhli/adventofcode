# https://adventofcode.com/2023/day/11
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'example.txt' and don't submit:
#     python3 python.py e
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2023 -d 11 -oi /dev/stdout | python3 python.py -
#     aocd 11 2023 | python3 python.py -
#     pbpaste | python3 python.py -

FACTOR1 = 2
FACTOR2 = 1_000_000

def solve(lines: list[str]) -> tuple[int, int]:
    space = []; space2 = []
    col_empty = [ True ] * len(lines[0])
    galaxies = []
    for i, line in enumerate(lines):
        space.append([])
        space2.append([])
        expand_row = int('#' not in line)
        for j, c in enumerate(line):
            space[-1].append(max(1, expand_row * FACTOR1))
            space2[-1].append(max(1, expand_row * FACTOR2))
            if c == '#':
                col_empty[j] = False
                galaxies.append((i, j))

    for j in range(len(space[0])):
        if col_empty[j]:
            for i in range(len(space)):
                space[i][j] = FACTOR1
                space2[i][j] = FACTOR2

    s = s2 = 0
    for g, ga in enumerate(galaxies):
        for g2 in range(g+1, len(galaxies)):
            x, y = ga
            x2, y2 = galaxies[g2]
            if x > x2: x2, x = x, x2
            if y > y2: y, y2 = y2, y
            s += sum(space[i][y] for i in range(x, x2)) + sum(space[x2][i] for i in range(y, y2))
            s2 += sum(space2[i][y] for i in range(x, x2)) + sum(space2[x2][i] for i in range(y, y2))
    return s, s2


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()

    ############################################################################

    s, s2 = solve(lines)
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=11, year=2023, reopen=False)
    print(s2)
    if inputfn == "input.txt":
        submit(s2, "b", day=11, year=2023, reopen=False)
