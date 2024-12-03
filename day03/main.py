import re


def part1():
    ans = 0
    lines = open('input.txt').read().splitlines()
    for line in lines:
        for match in re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", line):
            ans += int(match.group(1)) * int(match.group(2))

    print(f"Part 1: {ans}")


def part2():
    ans = 0
    lines = open('input.txt').read().splitlines()
    adding = True
    for line in lines:
        for match in re.finditer(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)", line):
            if match[0] == "do()":
                adding = True
            elif match[0] == "don't()":
                adding = False
            elif adding:
                ans += int(match.group(1)) * int(match.group(2))

    print(f"Part 2: {ans}")


if __name__ == "__main__":
    part1()
    part2()
