# https://adventofcode.com/2023/day/9
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
#     aoc d -y 2023 -d 9 -oi /dev/stdout | python3 python.py -
#     aocd 9 2023 | python3 python.py -
#     pbpaste | python3 python.py -


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = [ [ int(i) for i in line.split() ] for line in  f.read().splitlines() ]

    ############################################################################

    diffs = []
    for seq in lines:
        diff = [ seq ]
        curd: list[int] = [ 1 ]
        while any(curd):
            curd = []
            prevs = diff[-1]
            prev = prevs[0]
            for i in range(1, len(prevs)):
                curd.append(prevs[i] - prev)
                prev = prevs[i]
            diff.append(curd)
        diffs.append(diff)

    ############################################################################
    # part 1
    s = sum(sum(d[-1] for d in diff) for diff in diffs)
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=9, year=2023, reopen=False)

    ############################################################################
    # part 2
    s = sum(sum((-1)**i * d[0] for i, d in enumerate(diff)) for diff in diffs)
    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=9, year=2023, reopen=False)
