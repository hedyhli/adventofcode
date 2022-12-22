# https://adventofcode.com/2022/day/18
# cubezz
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2022 -d 18 -oi /dev/stdout | python3 python.py -
#     aocd 18 2022 | python3 python.py -
#
# Part 2 takes 4 mins to run?!


ADJ = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def isadj(a, b):
    """a has a face touching b's face"""
    diff = 0
    for i, j in zip(a, b):
        diff += abs(i-j)
    return diff <= 1

def is_out_bounds(a):
    """Cube a is beyond bounds of other cubes"""
    for i, v in enumerate(a):
        if minc[i] > v or maxc[i] < v:
            return True
    return False

def iteradj(a):
    """Iterate through adjacent positions"""
    for face in ADJ:
        yield tuple(a + b for a, b in zip(face, a))



if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else inputfn) as f:
        # [ (1,2,3), ... ]
        lines = list(tuple(map(int, line.split(','))) for line in f.read().splitlines())

    # part 1
    SA = 0  # total surface area
    for i, cube in enumerate(lines):
        SA += 6
        for cubecheck in lines[i+1:]:
            if isadj(cube, cubecheck):
                SA -= 2
    print(SA)
    if inputfn == "input.txt":
        submit(SA, "a", day=18, year=2022)

    # part 2
    # look for trapped air XD
    # get min max
    minc = [0, 0, 0]
    maxc = [0, 0, 0]
    for cube in lines:
        for i, v in enumerate(cube):
            if minc[i] > v:
                minc[i] = v
            if maxc[i] < v:
                maxc[i] = v

    ESA = 0
    # for progress updates
    total = len(lines)
    for i, cube in enumerate(lines):
        print(f"{i/total:.1f}%", end="\r")
        # for each neighbor
        for adjcube in iteradj(cube):
            if adjcube in lines:
                continue
            # the neighbor pos is no occupied with another cube
            visited = {adjcube,}
            queue = [adjcube]

            while queue:
                # until every touching neighbor is either visited (a cube) or
                # is out of the lava droplet's bounds?
                qcube = queue.pop(0)
                # stop searching, you'll only find more air
                if is_out_bounds(qcube):
                    ESA += 1
                    break
                # for each neighbor's neighbor
                for adjqcube in iteradj(qcube):
                    if adjqcube in visited or adjqcube in lines:
                        continue
                    # current pos is not a cube
                    visited.add(adjqcube)
                    queue.append(adjqcube)

    print(ESA)
    if ESA == SA:
        exit(1)
    if inputfn == "input.txt":
        submit(ESA, "b", day=18, year=2022)
