import re


batch = []
with open("input.txt") as f:
    batch = [ i.strip() for i in f.read().split("\n\n") ]

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_count = 0

for passport in batch:
    fields = set()
    for pair in passport.split():
        try:
            key, val = pair.split(":")
        except:
            pass
        if key != "cid":
            fields.add(key)
    if len(fields.symmetric_difference(required)) == 0:
        valid_count += 1

print(valid_count)

######################################################

ecl = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
valid_count = 0

for passport in batch:
    fail = False
    fields = { pair.split(":")[0]: pair.split(":")[1] for pair in passport.split() }
    fields.pop('cid', None)
    if not (len(required.symmetric_difference(set(fields.keys()))) == 0):
        # must continue all required keys
        continue
    for key in fields.keys():
        try:
            if key == 'byr':
                year = int(fields[key])
                assert 1920 <= year <= 2002

            elif key == 'iyr':
                year = int(fields[key])
                assert 2010 <= year <= 2020

            elif key == 'eyr':
                year = int(fields[key])
                assert 2020 <= year <= 2030

            elif key == 'hgt':
                assert fields[key].endswith('cm') or fields[key].endswith('in')
                height = int(fields[key][:-2])
                if fields[key].endswith('cm'):
                    assert 150 <= height <= 193
                elif fields[key].endswith('in'):
                    assert 59 <= height <= 76

            elif key == 'hcl':
                assert re.search(r"^#[0-9a-f]{6}$", fields[key])

            elif key == 'ecl':
                assert fields[key] in ecl

            elif key == 'pid':
                assert re.search(r"^\d{9}$", fields[key])

            else:
                # UNREACHABLE
                print(key, fields[key])
        except (AssertionError, ValueError) as e:
            fail = True

    if not fail:
        valid_count += 1

print(valid_count)
