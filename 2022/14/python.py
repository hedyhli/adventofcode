# solved but WIP!!!

from aocd import submit
# from pysnooper import snoop


# @snoop()
def hits_rock(sx, sy):
    """Whether sand at coords x,y HAS hit a rock below"""
    x = sx; y = sy# + 1
    for rock in rocks:
        # p = previous
        px = py = 0
        for point in rock:
            if px == py == 0:
                px = point[0]
                py = point[1]
                continue
            # n = now
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

    rocks = []  # input data not further parsed
    lowest = 0  # highest y-coordinate of rocks


    with open("input.txt") as f:
        for line in f.read().splitlines():
            rocks.append([])
            for coord in line.split(' -> '):
                x, y = tuple(map(int, coord.split(',')))
                if y > lowest:
                    lowest = y
                rocks[-1].append((x, y))


    sands = []  # stationary sand units
    # new sand unit
    # sand starts at 500,0
    sandx, sandy = 500, 0
    while True:
        print(len(sands), end="\r")
        if sandy >= lowest:
            # if it's below or equal to lowest rock level,
            # it will continue falling into the abyss
            # sandx, sandy = 500, 0
            # # hence, send new sand. stop tracking this one.
            # continue
            print(sandx, sandy)
            break


        if not hits_rock(sandx, sandy+1) and (sandx, sandy+1) not in sands:
            # continue going down until it hits a rock or another sand unit
            sandy += 1
            continue
        # has hit a rock or another sand unit
        # try       down-left,      then down-right
        # print(sands, sandx, sandy)
        for x, y in [(sandx-1, sandy+1), (sandx+1, sandy+1)]:
            if not hits_rock(x, y) and (x, y) not in sands:
                sandx, sandy = x, y
                break
        # print(sands, sandx, sandy)
        if sandx != x and sandy != y:
            # down-left and down-right doesn't work.
            # the sand unit is now stationary.
            sands.append((sandx, sandy))
            sandx, sandy = 500, 0  # send new sand


    # print(sands)
    print(s := len(sands))
    submit(s, "a", 14, 2022)

    # submit( , "b", 14, 2022)
