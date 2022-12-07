import re
# from typing import Tuple

from aocd import submit

with open("input.txt") as f:
    # List of tuples
    # [('nop', '+0'), ...]
    bootcode = [ tuple(line.strip().split()) for line in f.readlines() ]


ran_indexes = []  # List of bootcode indexes that have been run

def runcode(i: int = 0, acc: int = 0, reset: bool = False, flip_index: int = -1) -> tuple[int, bool]:
    """Run the boot code, return final acc value, and whether it properly terminates

    Parameters:
        i          (int)   index
        acc        (int)   acc value
        reset      (bool)  whether to reset the list of indexes of codes already ran
        flip_index (int)   the index of bootcode to which should flip nop/jmp
                           (set to -1 or under for none). The actual left operand of the
                           bootcode at index flip_index does not need to actually be nop/jmp

    Returns: Tuple of the final acc value, and whether it loops infinitely.
    """
    global ran_indexes
    # Success means, pointer have reached end of boot code, hence it terminates successfully
    if i == len(bootcode):
        return acc, False
    if reset: ran_indexes = []

    # It's an infinite loop as the current line of boot code has already been run before
    if i in ran_indexes:
        return acc, True

    # Begin runnign the current bootcode line
    ran_indexes.append(i)
    op, arg = bootcode[i]
    arg = int(arg)

    # Flip nop/jmp
    # if (op in (nj:=('nop', 'jmp'))) and i == flip_index:
    #     op = nj[(nj.index(op)+1)%2]
    op = nj[(nj.index(op)+1)%2] if op in (nj := ('nop', 'jmp')) and i == flip_index else op

    # Finally, parse the code.
    # Possible op codes:
    # - acc: add arg to the acc
    # - jmp: jump arg lines in the boot code to run another instruction
    # - nop: no operation
    if    op == 'acc':  acc += arg
    elif  op == 'jmp':  return runcode(i+arg, acc, flip_index=flip_index)
    # Proceed to next line (for acc and nop)
    return runcode(i+1, acc, flip_index=flip_index)


# False as ran_indexes was newly initiated - avoid extra assignment of new list object
print(a := runcode()[0])
submit(a, "a", 8, 2020)

inf = True; i = 0
while inf:
    if i == len(bootcode):
        print("FAIL"); break
    a, inf = runcode(reset=True, flip_index=i)
    i += 1

print(a)
submit(a, "b", 8, 2020)


# Old impl

# part 2
# one of the nop instructions changed to jmp, or vice verse, so that the program terminates without infinite looping
# oldcode = bootcode.copy()
# i = -1
# while not term:
#     bootcode[i] = oldcode[i]
#     i += 1
#     if i == len(bootcode):
#         print("FAIL")
#         break
#     op, arg = bootcode[i]
#     if op != 'acc':
#         bootcode[i] = ('jmp' if op == 'nop' else 'nop', arg)
#     else:
#         old = tuple()
#         continue
#     ran_indexes = []
#     a, term = runcode2(0, 0)
