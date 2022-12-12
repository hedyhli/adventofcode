import time


class Circuit:
    def __init__(self, instructions, X=1, spritewidth=3, coln=40):
        self.X = X
        self.spritewidth = spritewidth
        self.cycle = 0
        self.pos = 0
        self.coln = coln
        self.rows = [["."]*coln]
        self.strengthsum = 0
        self.instructions = instructions

    def tick(self):
        if abs(self.X-self.pos) < (self.spritewidth-1):
            self.rows[-1][self.pos] = '#'
        self.cycle += 1
        if self.cycle%40 == 0:
            self.rows.append(['.']*self.coln)
            self.pos = -1
        if (self.cycle-20)%40 == 0:
            self.strengthsum += self.X * self.cycle
        self.pos += 1

        # Live drawing!
        time.sleep(0.02)
        print(*self.rows[-1])  # Space between each char - final res more readable
        if not (self.cycle+1)%40 == 0:
            print("\033[1A", end="\x1b[2K")

    def execute(self):
        for ins in self.instructions:
            self.tick()
            ins = ins.split(" ")
            if ins[0] == "addx":
                self.tick()
                self.X += int(ins[1])
        self.rows.pop()

    def print_result(self):
        print("Signal strength sum:", self.strengthsum)
        print("Message:")
        print("\n".join("".join(row) for row in self.rows))


if __name__ == '__main__':
    with open("input.txt") as f:
        instructions = f.read().splitlines()
    c = Circuit(instructions)
    c.execute()
    print("Signal strength sum:", c.strengthsum)
