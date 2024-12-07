import itertools


def calc(columns, operators):
    ret = columns[0]
    for idx in range(len(operators)):
        if operators[idx] == "+":
            ret += columns[idx + 1]
        elif operators[idx] == "*":
            ret *= columns[idx + 1]
        elif operators[idx] == "||":
            ret = int(str(ret) + str(columns[idx + 1]))
        else:
            raise Exception(f"Invalid op {operators[idx]}")

    return ret


def part1():
    lines = open('input.txt').read().splitlines()

    ans = 0
    for line in lines:
        test_value, columns = line.split(": ")
        test_value = int(test_value)
        columns = list(map(int, columns.split(" ")))

        ops = [list(op) for op in itertools.product(["+", "*"], repeat=len(columns) - 1)]
        for op in ops:
            if calc(columns, op) == test_value:
                ans += test_value
                break

    return ans


def part2():
    lines = open('input.txt').read().splitlines()

    ans = 0
    for line in lines:
        test_value, columns = line.split(": ")
        test_value = int(test_value)
        columns = list(map(int, columns.split(" ")))

        ops = [list(op) for op in itertools.product(["+", "*", "||"], repeat=len(columns) - 1)]
        for op in ops:
            if calc(columns, op) == test_value:
                ans += test_value
                break

    return ans


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
