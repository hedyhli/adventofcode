import re

from aocd import submit


with open("input.txt") as f:
    lines = f.read().strip().split("\n")


parse_name = re.compile(r"^(\w+ \w+) bags contain")
parse_contents = re.compile(r"\d+ (\w+ \w+) bags?[, ]?")


def part1(lines: list) -> int:
    #                 {str:  set,}
    bag_rules = {}  # {name: {contents names...}}
    entries = {"shiny gold"}

    for line in lines:
        bag_name = parse_name.findall(line).pop()
        bag_rules[bag_name] = set()
        for bag in parse_contents.finditer(line.split("contain")[1].strip()):
            bag_rules[bag_name].add(bag.groups()[0])

    for _ in range(len(lines)//4):
        for bag_name in bag_rules.keys():
            common = bag_rules[bag_name] & entries
            if len(common) == 0:
                continue
            entries.add(bag_name)

    return len(entries) - 1


def part2(lines: list) -> int:
    parse_contents = re.compile(r"(\d+) (\w+ \w+) bags?[, ]?")
    #                 {str:  {str:           int,},}
    bag_rules = {}  # {name: {contents name: num, ...}}

    for line in lines:
        bag_name = parse_name.findall(line).pop()
        bag_rules[bag_name] = {}
        for bag in parse_contents.finditer(line.split("contain")[1].strip()):
            bag_rules[bag_name][bag.groups()[1]] = int(bag.groups()[0])

    def dig(dig_name: str="shiny gold") -> int:
        # Unneeded as dig() returns 0 if no other bags in this one
        # n = 0, and n is not altered in for loop (nothing happens),
        # hence return n, is returning 0.
        # :
        # if len(bag_rules[dig_name]) == 0:
        #     return 1
        n = 0
        for bag_name in bag_rules[dig_name].keys():
            if len(bag_rules[bag_name]) == 0:
                n += bag_rules[dig_name][bag_name]
                continue
            #    bag in bag    * num of those                  + num of current bag
            n += dig(bag_name) * bag_rules[dig_name][bag_name] + bag_rules[dig_name][bag_name]
        return n

    n = dig()
    return n


num_entries = part1(lines)
print(num_entries)
submit(num_entries, year=2020, day=7, part="a")

n = part2(lines)
print(n)
submit(n, year=2020, day=7, part="b")
