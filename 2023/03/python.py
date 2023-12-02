# https://adventofcode.com/2023/day/3
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
#     aoc d -y 2023 -d 3 -oi /dev/stdout | python3 python.py -
#     aocd 3 2023 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce



if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()



    # part 1
    print()
    # if inputfn == "input.txt":
    #     submit(, "a", day=3, year=2023, reopen=False)



    # part 2
    print()
    # if inputfn == "input.txt":
    #     submit(, "b", day=3, year=2023, reopen=False)
