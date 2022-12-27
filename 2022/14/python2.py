

def hits_rock(sx, sy):
    """Whether sand at coords x,y HAS hit a rock below"""

    x = sx; y = sy

    for rock in rocks:
        px = py = 0
        for point in rock:
            if px == py == 0:
                px, py = point
                continue
            nx, ny = point

            # comparison
            ax, ay = px, py
            bx, by = point

            # swap if drawn in reverse
            if ax >= bx and ay >= by:
                ax, bx = bx, ax
                ay, by = by, ay

            if ay == by == y:
                # horz line
                if ax <= x <= bx:
                    return True
            elif ax == bx == x:
                # vert line
                if ay <= y <= by:
                    return True

            px, py = nx, ny
    return False



if __name__ == '__main__':

    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from collections import deque

    from aocd import submit

    rocks = []  # input data not further parsed
    lowest = 0  # highest y-coordinate of rocks


    with open(0 if inputfn == '-' else inputfn) as f:
        for line in f.read().splitlines():
            rocks.append([])
            for coord in line.split(' -> '):
                x, y = tuple(map(int, coord.split(',')))
                if y > lowest:
                    lowest = y
                rocks[-1].append((x, y))

    floor = lowest + 2
    print(floor)
    sands = deque()  # stationary sand units
    n = 0
    # new sand unit
    # sand starts at 500,0
    sandx, sandy = 500, 0
    while '500,0' not in sands:
        if len(sands) > 76: # arbitrary 80
            sands.popleft()
        print(n, end="\r")

        if not hits_rock(sandx, sandy+1) and f'{sandx},{sandy+1}' not in sands:
            # continue going down until it hits a rock or another sand unit
            if sandy+1 == floor-1:
                # hit the floor, baby
                sands.append(f'{sandx},{sandy+1}')
                n += 1
                sandx, sandy = 500, 0  # send new sand
                continue
            sandy += 1
            continue
        # has hit a rock or another sand unit
        # try       down-left,      then down-right
        # print(sands, sandx, sandy)
        for x, y in [(sandx-1, sandy+1), (sandx+1, sandy+1)]:
            if not hits_rock(x, y) and f'{x},{y}' not in sands:
                sandx, sandy = x, y
                break

        if sandy == floor-1 or (sandx != x and sandy != y):
            # it has hit the floor, OR,
            #
            # down-left and down-right doesn't work.
            # the sand unit is now stationary.
            sands.append(f'{sandx},{sandy}')
            n += 1
            sandx, sandy = 500, 0  # send new sand


    print(n)
    # submit(s, "a", 14, 2022)

    if inputfn == "input.txt":
        submit(n, "b", 14, 2022)
