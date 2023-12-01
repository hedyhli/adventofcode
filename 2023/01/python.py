# https://adventofcode.com/2023/day/1
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2023 -d 1 -oi /dev/stdout | python3 python.py -
#     aocd 1 2023 | python3 python.py -


if __name__ == '__main__':

    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    with open(0 if inputfn == '-' else inputfn) as f:
        lines = f.read().splitlines()

    s = 0
    for line in lines:
        t = ''.join(filter(lambda x: x.isdigit(), line))
        t = t[0] + t[-1]
        s += int(t)

    # part 1
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=1, year=2023)

    D = ['one','two','three','four','five','six','seven','eight','nine']

    s = 0
    for line in lines:
        li = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                li.append(line[i])
            else:
                for d in range(len(D)):
                    if line[i:].startswith(D[d]):
                        # No two items a,b in D where a[-2:]==b[1:]
                        i += len(D[d])-1-2
                        li.append(str(d+1))
                        break
            i += 1

        s += int(li[0] + li[-1])

    # part 2
    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=1, year=2023)
