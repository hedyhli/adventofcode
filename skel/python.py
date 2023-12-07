# https://adventofcode.com/YEAR/day/DAY
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
#     aoc d -y YEAR -d DAY -oi /dev/stdout | python3 python.py -
#     aocd DAY YEAR | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce
# from collections import
# from itertools import
# import math


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()

    ############################################################################


    ############################################################################
    # part 1


    print()
    # if inputfn == "input.txt":
    #     submit(, "a", day=DAY, year=YEAR, reopen=False)


    ############################################################################
    # part 2


    print()
    # if inputfn == "input.txt":
    #     submit(, "b", day=DAY, year=YEAR, reopen=False)
