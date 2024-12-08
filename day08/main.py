def part1():
    lines = open('input.txt').read().splitlines()

    antennas = []
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] != ".":
                antennas.append((lines[r][c], r,c))

    anti = set()
    for a1 in antennas:
        for a2 in antennas:
            if a1 == a2:
                continue

            if a1[0] != a2[0]:
                continue

            nr = a1[1] + a1[1] - a2[1]
            nc = a1[2] + a1[2] - a2[2]

            if nr in range(len(lines)) and nc in range(len(lines[0])):
                anti.add((nr,nc))

    return len(anti)

def part2():
    lines = open('input.txt').read().splitlines()

    antennas = []
    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] != ".":
                antennas.append((lines[r][c], r,c))

    anti = set()
    for a1 in antennas:
        for a2 in antennas:
            if a1 == a2:
                continue

            if a1[0] != a2[0]:
                continue

            mul = 0
            while True:
                nr = a1[1] + ((a1[1] - a2[1]) * mul)
                nc = a1[2] + ((a1[2] - a2[2]) * mul)

                if nr in range(len(lines)) and nc in range(len(lines[0])):
                    anti.add((nr, nc))
                else:
                    break

                mul += 1

    return len(anti)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
