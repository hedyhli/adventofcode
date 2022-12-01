# ! WIP
# Binary search! how exciting :D

# First 7 chars
# choose 0 to 127 incl
# F = lower, B = upper
#
# Last 3 chars
# choose 0 to 7 incl
# L = lower, R = upper


def get_code(code):
    # inclusive
    rbot = 0
    rtop = 127
    cbot = 0
    ctop = 7

    for char in code:
        if char == 'F':
            rtop -= (rtop-rbot) // 2 + 1
        if char == 'B':
            rbot += (rtop-rbot) // 2 + 1
        if char == 'L':
            ctop -= (ctop-cbot) // 2 + 1
        if char == 'R':
            cbot += (ctop-cbot) // 2 + 1

    if rbot == rtop:
        return rbot
    if cbot == ctop:
        return cbot
    raise "Error :o seat code cannot be determined " + str(rowcode)


if __name__ == '__main__':
    seats = []
    with open("input.txt") as f:
        seats = [ i.strip() for i in f.readlines() ]

    # seats = [
    #     'BFFFBBFRRR',
    #     'FFFBBBFRRR',
    #     'BBFFBBFRLL',
    # ]

    seat_IDs = []

    for seatcode in seats:
        row = get_code(seatcode[:-3])
        col = get_code(seatcode[7:])
        seat_IDs.append(row * 8 + col)

    print(max(seat_IDs))
