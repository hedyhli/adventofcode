# https://adventofcode.com/2023/day/18
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
#     aoc d -y 2023 -d 18 -oi /dev/stdout | python3 python.py -
#     aocd 18 2023 | python3 python.py -
#     pbpaste | python3 python.py -

RDLU = (1, -1j, -1, 1j)

def parse(lines: list[str]):
    return zip(*(
        (RDLU['RDLU'.index(a)] * int(b),
         RDLU[int(c[7])]       * int(c[2:7], 16))
        for a, b, c in map(str.split, lines)
    ))

def lagoon_capacity(moves: list[complex]):
    cur = prev = 0
    return 1 + sum((
            ((cur:=cur+m).real - prev.real) * (cur.imag + prev.imag) + abs(m) + 0*(prev:=cur)
        ) / 2 for m in moves).real

if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit
    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines() 


    ############################################################################
    # part 1 and 2

    s = [ lagoon_capacity(moves) for moves in parse(lines) ]

    print(*s, sep='\n')
    if inputfn == "input.txt":
        submit(s[0], "a", day=18, year=2023, reopen=False)
        submit(s[1], "b", day=18, year=2023, reopen=False)
