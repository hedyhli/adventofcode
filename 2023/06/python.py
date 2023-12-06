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

from functools import reduce

if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()

    times = [ int(i.strip()) for i in lines[0].split(':  ')[1].strip().split() ]
    dists = [ int(i.strip()) for i in lines[1].split(':  ')[1].strip().split() ]

    # part 1
    prod = 1
    for i in range(len(times)):
        ways = 0
        for hold in range(1, times[i]):
            left = times[i] - hold
            d = left * hold
            if d > dists[i]:
                ways += 1
        prod *= ways

    print(prod)
    if inputfn == "input.txt":
        submit(prod, "a", day=6, year=2023, reopen=False)


    # part 2 setup
    time = int(reduce(lambda x,y: str(x)+str(y), times, ''))
    dist = int(reduce(lambda x,y: str(x)+str(y), dists, ''))

    # part 2
    ways = 0
    for hold in range(1, time):
        left = time - hold
        d = left * hold
        if d > dist:
            ways += 1

    print(ways)
    if inputfn == "input.txt":
        submit(ways, "b", day=6, year=2023, reopen=False)
