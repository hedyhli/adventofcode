# ah yes working on visualization
# WIP!!!!!!!
# (the puzzle is solved though)

from collections import deque
import time

from aocd import submit

with open("input.txt") as f:
    lines = list(list(map(ord, line)) for line in f.read().splitlines())

for i, line in enumerate(lines):
    try:
        j = line.index(ord('S'))
        S_pos = (i, j)
        line[j] = ord("a")
    except: pass

    try:
        j = line.index(ord('E'))
        E_pos = (i, j)
        line[j] = ord("z")
    except: pass


dq = deque()

def walk(reverse=False):
    if reverse:
        dq.append((0, E_pos[0], E_pos[1]))
        visited = [E_pos]
    else:
        dq.append((0, S_pos[0], S_pos[1]))
        visited = [S_pos]

    while dq:
        yield dq
        n, row, col = dq.popleft()
        u = (row-1, col)
        d = (row+1, col)
        l = (row, col-1)
        r = (row, col+1)

        for newr, newc in u, d, l, r:
            if (newr, newc) in visited:
                continue
            if newr < 0 or newc < 0 or newr >= len(lines) or newc >= len(lines[0]):
                continue

            if reverse:
                # Part 2
                if lines[row][col] - lines[newr][newc] > 1:
                    continue
            else:
                # Part 1
                if lines[newr][newc] - lines[row][col] > 1:
                    continue

            if reverse:
                if lines[newr][newc] == ord('a'):
                    return n + 1
            else:
                if (newr, newc) == E_pos:
                    print(n+1)
                    return n + 1

            dq.append((n+1, newr, newc))
            visited.append((newr, newc))
            # don't break here, so other possibilities are kept in deque



# print(result := walk())
# submit(result, "a", 12, 2022)

# print(result := walk(True))
# submit(result, "b", 12, 2022)

if __name__ == '__main__':
    from curses import wrapper

    logf = open("log.txt", "a")

    def tui(stdscr) -> str:
        # while stdscr.getkey() != 'q':
            for q in walk():
                logf.write(str(q) + "\n")
                time.sleep(0.1)
                stdscr.clear()
                stdscr.refresh()
                n_list = []

                for i, line in enumerate(lines):
                    for j, o in enumerate(line):
                        ch = chr(o)
                        for n, row, col in q:
                            n_list.append(n)
                            if i == row and j == col:
                                stdscr.addstr("_")
                            else:
                                stdscr.addstr(ch)
                    stdscr.addstr("\n")
                stdscr.addstr("n_list: {n_list}")

    wrapper(tui)
    logf.close()
