# https://adventofcode.com/2020/day/10
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2020 -d 10 -oi /dev/stdout | python3 python.py -
#     aocd 10 2020 | python3 python.py -



if __name__ == '__main__':

    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else inputfn) as f:
        lines = f.read().splitlines()



    # part 1
    print()
    if inputfn == "input.txt":
        submit(, "a", day=10, year=2020)



    # part 2
    print()
    if inputfn == "input.txt":
        submit(, "b", day=10, year=2020)
