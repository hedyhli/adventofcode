from aocd import submit


with open("input.txt") as f:
    inp = f.read()


count = 0
for group in inp.split('\n\n'):
    ques = set(group.replace('\n', ''))
    count += len(ques)

print(count)
submit(count, part="a", year=2020, day=6)


count = 0
for group in inp.split('\n\n'):
    group = group.rstrip()
    if '\n' not in group:
        # only 1 person
        count += len(set(group))
        continue
    people = [ set(i) for i in group.split('\n') ]
    count += len(people[0].intersection(*people[1:]))

print(count)
submit(count, part="b", year=2020, day=6)


####################
# old implementation

# count = 0
# for group in inp.split('\n\n'):
#     qlist = []
#     for question in set(group.split('\n')[0]):
#         qlist.append(question)
#     newqlist = qlist.copy()
#     # loop through people other than the first
#     for person in group.split('\n')[1:]:
#         for question in newqlist:
#             nextperson = False
#             print(qlist)
#             if question not in person:
#                 qlist.pop(qlist.index(question))
#                 nextperson = True
#                 break
#             if nextperson:
#                 break
#     count += len(qlist)
# print(count)
