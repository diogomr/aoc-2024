def xmas_count(map, x, y):
    if map[x][y] != "X":
        return 0

    possible_dirs = [
        # Horizontal
        {"M": (0, 1), "A": (0, 2), "S": (0, 3)},
        {"M": (0, -1), "A": (0, -2), "S": (0, -3)},
        # Vertical
        {"M": (1, 0), "A": (2, 0), "S": (3, 0)},
        {"M": (-1, 0), "A": (-2, 0), "S": (-3, 0)},
        # Diagonal
        {"M": (1, 1), "A": (2, 2), "S": (3, 3)},
        {"M": (1, -1), "A": (2, -2), "S": (3, -3)},
        {"M": (-1, -1), "A": (-2, -2), "S": (-3, -3)},
        {"M": (-1, 1), "A": (-2, 2), "S": (-3, 3)}
    ]

    count = 0
    for direction in possible_dirs:
        count += 1
        for (target, (dx, dy)) in direction.items():
            if x + dx not in range(len(map)):
                count -= 1
                break
            if y + dy not in range(len(map[x])):
                count -= 1
                break

            if map[x + dx][y + dy] != target:
                count -= 1
                break

    return count


def is_two_max(map, x, y):
    if map[x][y] != "A":
        return False

    possible_dirs = [
        {(1, -1): "M", (-1, -1): "M", (1, 1): "S", (-1, 1): "S"},
        {(1, -1): "S", (-1, -1): "M", (1, 1): "S", (-1, 1): "M"},
        {(1, -1): "S", (-1, -1): "S", (1, 1): "M", (-1, 1): "M"},
        {(1, -1): "M", (-1, -1): "S", (1, 1): "M", (-1, 1): "S"},
    ]

    count = 0
    for direction in possible_dirs:
        count += 1
        for ((dx, dy), target) in direction.items():
            if x + dx not in range(len(map)):
                count -= 1
                break
            if y + dy not in range(len(map[x])):
                count -= 1
                break
            if map[x + dx][y + dy] != target:
                count -= 1
                break

    return count != 0


def part1():
    ans = 0
    lines = open('input.txt').read().splitlines()
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            ans += xmas_count(lines, x, y)

    print(f"Part 1: {ans}")


def part2():
    ans = 0
    lines = open('input.txt').read().splitlines()
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if is_two_max(lines, x, y):
                ans += 1

    print(f"Part 2: {ans}")


if __name__ == "__main__":
    part1()
    part2()
