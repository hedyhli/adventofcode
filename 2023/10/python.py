# https://adventofcode.com/2023/day/10
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
#     aoc d -y 2023 -d 10 -oi /dev/stdout | python3 python.py -
#     aocd 10 2023 | python3 python.py -
#     pbpaste | python3 python.py -

if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit

    grid:list[list[str]] = []
    # True if covered by path
    bgrid:list[list[bool]] = []
    # True if connects to borders of input
    # Assume none connects to borders first
    cgrid:list[list[bool]] = []
    dots = []

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        for i, line in enumerate(f.read().splitlines()):
            if 'S' in line:
                S = (i, line.index('S'))
            if '.' in line:
                for j, c in enumerate(line):
                    if c == '.':
                        dots.append((i, j))
            grid.append(list(line))
            bgrid.append([False] * len(line))
            cgrid.append([False] * len(line))

    tr = len(grid)
    tc = len(grid[0])

    ############################################################################
    # part 1

    x, y = S
    # neighbors of S
    stack = []
    if grid[x][y-1] in '-LF':
        stack.append((x, y-1))
    if grid[x][y+1] in '-7J':
        stack.append((x, y+1))
    if grid[x-1][y] in '|7F':
        stack.append((x-1, y))
    if grid[x+1][y] in '|JL':
        stack.append((x+1, y))

    depths = [0, 0, 0, 0]
    prev = S
    bgrid[S[0]][S[1]] = True

    while stack:
        x, y = stack.pop()
        depth = depths.pop()
        depth += 1

        if not (0 <= x < tr) or not (0 <= y < tc):
            bgrid[prev[0]][prev[1]] = False
            continue

        c = grid[x][y]

        if c == '.':
            bgrid[prev[0]][prev[1]] = False
            continue

        if c == 'S':
            break

        bgrid[x][y] = True

        if c == '|':
            for cur in ((x-1, y), (x+1, y)):
                if cur != prev:
                    break
        elif c == '-':
            for cur in ((x, y-1), (x, y+1)):
                if cur != prev:
                    break
        elif c == '7':
            for cur in ((x+1, y), (x, y-1)):
                if cur != prev:
                    break
        elif c == 'F':
            for cur in ((x, y+1), (x+1, y)):
                if cur != prev:
                    break
        elif c == 'J':
            for cur in ((x, y-1), (x-1, y)):
                if cur != prev:
                    break
        elif c == 'L':
            for cur in ((x, y+1), (x-1, y)):
                if cur != prev:
                    break

        prev = (x, y)
        stack.append(cur)
        depths.append(depth)


    if inputfn.startswith('example'):
        for row in bgrid:
            for col in row:
                print(int(col), end = '')
            print()

    depth//=2
    print(depth)
    if inputfn == "input.txt":
        submit(depth, "a", day=10, year=2023, reopen=False)

    ############################################################################
    # part 2

    tiles = 0
    pr = None
    for i in range(tr):
        inside = False
        j = 0
        while j < tc:
            c = grid[i][j]

            if not bgrid[i][j]:
                if inside:
                    tiles += 1
                j += 1
                continue

            if c in '|S':
                inside = not inside
                j += 1
                continue

            if c in 'FL':
                while j < tc and bgrid[i][j] and (d := grid[i][j]) not in 'J7':
                    j += 1
                if c == 'F' and d == 'J' or c == 'L' and d == '7':
                    inside = not inside
                j += 1


    print(tiles)
    if inputfn == "input.txt":
        submit(tiles, "b", day=10, year=2023, reopen=False)
