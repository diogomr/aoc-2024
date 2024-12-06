def part1():
    lines = open('input.txt').read().splitlines()
    lab_map = {}

    dirs = ["<", "^", ">", "v"]

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
        if nx not in range(len(lines[0])) or ny not in range(len(lines)):
            break

        if lab_map[(nx, ny)] == "#":
            direction = dirs[(dirs.index(direction) + 1) % 4]
        else:
            lab_map[(nx, ny)] = "X"
            guard = next_pos

    ans = 0
    for val in lab_map.values():
        if val == "X":
            ans += 1
    return ans

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
