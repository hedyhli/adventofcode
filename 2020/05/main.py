# ! WIP
# Binary search! how exciting :D


seats = []
with open("input.txt") as f:
    seats = [ i.strip() for i in f.readlines() ]


maxrow = 127
maxcol = 8

for seatcode in seats:
    rowcode = seatcode[:-3]
    colcode = seatcode[7:]
    print(rowcode, colcode)
