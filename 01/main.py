with open("input.txt") as f:
    inp = f.read().split('\n\n')

# part 1

# totals = []
# for elf in elves:
#     print(elf)
#     total = sum([ int(i.strip()) for i in elf.split() ])
#     totals.append(total)

print("Highest")
print(max( sum(int(j.strip()) for j in i.split()) for i in inp ))


# part 2
# print(totals.pop(totals.index(max(totals))))
# print(totals.pop(totals.index(max(totals))))
# print(totals.pop(totals.index(max(totals))))

print("Sum of highest 3")
print(sum( sorted( (sum(int(j.strip()) for j in i.split()) for i in inp), reverse=True)[:3] ))
