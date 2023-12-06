# https://adventofcode.com/2023/day/6
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
#     aoc d -y 2023 -d 6 -oi /dev/stdout | python3 python.py -
#     aocd 6 2023 | python3 python.py -
#     pbpaste | python3 python.py -

import math


def get_ways(time:int, dist:int) -> int:
    """
    Uses quadratic formula to get the number of integers between
    roots.
    """
    det = math.sqrt(time**2 - 4 * dist)
    root1 = (time - det)/2
    root2 = (time + det)/2
    return math.ceil(root2) - 1 - math.floor(root1);

if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit  # noqa: ignore
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()


    # parse
    times = [ int(i.strip()) for i in lines[0].split(':  ')[1].strip().split() ]
    dists = [ int(i.strip()) for i in lines[1].split(':  ')[1].strip().split() ]

    # part 1
    part1 = math.prod(get_ways(times[i], dists[i]) for i in range(len(times)))

    # part 2
    time = int(''.join(str(t) for t in times))
    dist = int(''.join(str(d) for d in dists))
    part2 = get_ways(time, dist)

    # check answer
    print(part1)
    if inputfn == "input.txt":
        submit(part1, "a", day=6, year=2023, reopen=False)
    print(part2)
    if inputfn == "input.txt":
        submit(part2, "b", day=6, year=2023, reopen=False)
