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

    seat_IDs = []

    # Part 1
    for seatcode in seats:
        row = get_code(seatcode[:-3])
        col = get_code(seatcode[7:])
        seat_IDs.append(row * 8 + col)

    print("Highest seat number was", max(seat_IDs))

    # Part 2

    seat_IDs = sorted(seat_IDs)
    prev = seat_IDs[0]
    your_seat = 0
    for seat_ID in seat_IDs[1:]:
        if seat_ID - prev > 1:
            your_seat = seat_ID-1
            break
        prev = seat_ID

    print("Your seat was", your_seat)
