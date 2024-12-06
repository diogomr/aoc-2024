dirs = ["<", "^", ">", "v"]


def is_stuck(guard, direction, lab_map, xmax, ymax):
    while True:
        x, y = guard

        if direction == "^":
            next_pos = (x, y - 1)
        elif direction == "v":
            next_pos = (x, y + 1)
        elif direction == "<":
            next_pos = (x - 1, y)
        elif direction == ">":
            next_pos = (x + 1, y)
        else:
            raise f"Invalid direction {direction}"

        nx, ny = next_pos
        if nx not in range(xmax) or ny not in range(ymax):
            return False

        if lab_map[(nx, ny)] == "#":
            direction = dirs[(dirs.index(direction) + 1) % 4]
        else:
            if lab_map[(nx, ny)] == "X":
                lab_map[(nx, ny)] = "X2"
                guard = next_pos
            elif lab_map[(nx, ny)] == "X2":
                lab_map[(nx, ny)] = "X3"
                guard = next_pos
            elif lab_map[(nx, ny)] == "X3":
                return True
            else:
                lab_map[(nx, ny)] = "X"
                guard = next_pos


def part2():
    lines = open('input.txt').read().splitlines()
    lab_map = {}

    guard = None
    direction = None
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] in dirs:
                guard = (x, y)
                direction = lines[y][x]
                lab_map[(x, y)] = "X"
            else:
                lab_map[(x, y)] = lines[y][x]

    ans = 0
    xmax = len(lines[0])
    ymax = len(lines)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lab_map[(x, y)] == "X" or lab_map[(x, y)] == "#":
                continue

            copy_map = lab_map.copy()
            copy_map[(x, y)] = "#"

            if is_stuck(guard, direction, copy_map, xmax, ymax):
                ans += 1

    return ans


if __name__ == "__main__":
    print(f"Part 2: {part2()}")
