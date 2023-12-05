# https://adventofcode.com/2023/day/5
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
#     aoc d -y 2023 -d 5 -oi /dev/stdout | python3 python.py -
#     aocd 5 2023 | python3 python.py -
#     pbpaste | python3 python.py -

# from functools import reduce


def conv(seed, m) -> int:
    for b, n in m.keys():
        s = seed - b
        if 0 <= s <= n:
            # print(b, n, m[(b,n)] + s)
            return m[(b,n)] + s
    return seed


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        seeds: list[int] = [int(i) for i in f.readline()[7:].strip().split(' ')]
        f.readline()
        sections: list[list[str]] = [ i.strip().split('\n') for i in f.read().split('\n\n') ]


    maxnum = 0
    M:list = []
    for sec in sections:
        M.append({})
        for line in sec[1:]:
            a, b, n = [int(i) for i in line.strip().split(' ')]
            M[-1][(b, n)] = a
            maxnum = max(maxnum, b + n)

    maxnum += 1
    ans = maxnum
    for seed in seeds:
        for m in M:
            seed = conv(seed, m)
        ans = min(ans, seed)

    # part 1
    print(ans)
    if inputfn == "input.txt":
        submit(ans, "a", day=5, year=2023, reopen=False)


    D = {}
    ans = 10**11
    s = 0
    while s < len(seeds):
        print(len(seeds)-s)
        start, n = seeds[s], seeds[s + 1]
        s += 2
        for seed in range(start, start+n):
            if final := D.get(seed):
                ans = min(ans, final)
                continue
            initial = seed
            for m in M:
                seed = conv(seed, m)
            ans = min(ans, seed)
            D[initial] = seed
        print("\033[1A", end="\x1b[2K")

    # part 2
    print()
    print(ans)
    # if inputfn == "input.txt":
    #     submit(ans, "b", day=5, year=2023, reopen=False)
