# https://adventofcode.com/2023/day/4
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
#     aoc d -y 2023 -d 4 -oi /dev/stdout | python3 python.py -
#     aocd 4 2023 | python3 python.py -
#     pbpaste | python3 python.py -


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        lines = f.read().splitlines()


    cards = []
    for line in lines:
        parts = line.split(': ')[1].split(' | ')
        parts[0], parts[1] = parts[0].strip(), parts[1].strip()
        cards.append((
            [int(i.strip()) for i in parts[0].split()],
            [int(i.strip()) for i in parts[1].split()]
        ))

    # part 1
    matches = {}
    s = 0
    for i, C in enumerate(cards):
        n = 0.5
        m = 0
        for win in C[0]:
            if win in C[1]:
                n *= 2
                m += 1
        n = int(n)
        matches[i+1] = m
        s += n

    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=4, year=2023, reopen=False)


    copies = {}
    for i in matches.keys():
        copies[i] = 1

    # part 2
    for i, m in matches.items():
        for j in range(i+1, i+m+1):
            copies[j] += copies[i]

    s = sum(v for i, v in copies.items())

    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=4, year=2023, reopen=False)
