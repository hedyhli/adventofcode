# https://adventofcode.com/2023/day/7
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
#     aoc d -y 2023 -d 7 -oi /dev/stdout | python3 python.py -
#     aocd 7 2023 | python3 python.py -
#     pbpaste | python3 python.py -

from collections import Counter

strength  = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
strength2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def get_rank(c: Counter):
    coms = [ i[1] for i in c.most_common() ]
    if coms[0] == 5:
        return 7
    if coms[0] == 4:
        return 6
    if coms[0] == 3 and coms[1] == 2:
        return 5
    if coms[0] == 3:
        return 4
    if coms[0] == 2 and coms[1] == 2:
        return 3
    if coms[0] == 2:
        return 2
    if coms[0] == 1:
        return 1
    raise ValueError


if __name__ == '__main__':
    import sys
    inputfn = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    from aocd import submit

    with open(0 if inputfn == '-' else \
              ('example.txt' if inputfn == 'e' else inputfn)) as f:
        hands = []
        for line in f.read().splitlines():
            cards, bid = line.split()
            hands.append((
                Counter(cards),                      # Frequency
                [strength.index(i) for i in cards],  # Strengths
                int(bid),                            # Bid
                cards                                # Original cards
            ))

    ############################################################################
    # part 1
    #                 rank strengths  bid  cards (for debugging)
    ranks: list[tuple[int, list[int], int, str]] = []
    for hand in hands:
        ranks.append((get_rank(hand[0]), hand[1], hand[2], hand[3]))

    ranks.sort()
    s = sum((r+1) * p[2] for r, p in enumerate(ranks))

    print(s)
    if inputfn == "input.txt":
        submit(s, "a", day=7, year=2023, reopen=False)


    ############################################################################
    # part 2
    ranks = []
    for hand in hands:
        c = hand[0]
        cards = hand[3]
        q = [ strength2.index(i) for i in cards ]

        if cards != 'JJJJJ':
            common = c.most_common(2)
            best = common[0][0]
            if best == 'J':
                best = common[1][0]
            c = Counter(cards.replace('J', best))

        ranks.append((get_rank(c), q, hand[2], cards))

    ranks.sort()
    s = sum((r+1) * p[2] for r, p in enumerate(ranks))

    print(s)
    if inputfn == "input.txt":
        submit(s, "b", day=7, year=2023, reopen=False)
