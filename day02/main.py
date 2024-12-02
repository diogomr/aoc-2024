def is_safe(report):
    up = False
    down = False

    for i in range(1, len(report)):
        if report[i - 1] - report[i] > 0:
            down = True
        else:
            up = True

        if up and down:
            return False

        diff = abs(report[i - 1] - report[i])
        if diff < 1 or diff > 3:
            return False

    return True


def part1():
    lines = open('input.txt').read().splitlines()

    ans = 0
    for line in lines:
        line = list(map(int, line.split()))

        if is_safe(line):
            ans += 1

    print(f"Part 1: {ans}")


def part2():
    lines = open('input.txt').read().splitlines()

    ans = 0
    for line in lines:
        line = list(map(int, line.split()))

        if is_safe(line):
            ans += 1
        else:
            for i in range(len(line)):
                line_copy = list(line)
                del line_copy[i]

                if is_safe(line_copy):
                    ans += 1
                    break

    print(f"Part 2: {ans}")


if __name__ == "__main__":
    part1()
    part2()
