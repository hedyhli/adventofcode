# https://adventofcode.com/2023/day/2
#
## USAGE ##
# Run with 'input.txt' and submit with aocd:
#     python3 python.py
# Run with 'test.txt' and don't submit:
#     python3 python.py test.txt
# Run with stdin and don't submit:
#     cat myinput | python3 python.py -
#     aoc d -y 2023 -d 2 -oi /dev/stdout | python3 python.py -
#     aocd 2 2023 | python3 python.py -



if __name__ == '__main__':

    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    from aocd import submit

    games = []
    with open(0 if inputfn == '-' else inputfn) as f:
        for line in f.read().splitlines():
            conf = line.split(': ')[1].split('; ')
            indiv = []
            for c in conf:
                r = b = g = 0
                for spec in c.split(', '):
                    no, color = spec.split(' ')
                    no = int(no)
                    if color == 'blue':
                        b = no
                    elif color == 'red':
                        r = no
                    else:
                        g = no
                indiv.append((r, b, g))
            games.append(indiv)

    R = 12
    B = 14
    G = 13

    s = 0

    for g in range(len(games)):
        confs = games[g]
        ok = True
        for game in confs:
            if game[0] > R or game[1] > B or game[2] > G:
                ok = False
                break
        if ok:
            s += g+1

    # part 1
    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=2, year=2023)

    s = 0
    for i in range(len(games)):
        r, b, g = games[i][0]
        for game in games[i]:
            r = max(r, game[0])
            b = max(b, game[1])
            g = max(g, game[2])

        s += r * b * g

    # part 2
    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=2, year=2023)
