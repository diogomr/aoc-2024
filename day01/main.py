def input_file():
    return open('./day01/input.txt')


def part1():
    lines = input_file().read().splitlines()

    left, right = list(), list()

    for line in lines:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    res = []
    for i in range(len(left)):
        res.append(abs(left[i] - right[i]))

    print(f'Part 1: {sum(res)}')


def part2():
    lines = input_file().read().splitlines()

    left_arr = []
    right_counters = {}

    for line in lines:
        left, right = line.split("   ")
        left_arr.append(int(left))

        right_int = int(right)
        if right_int in right_counters:
            right_counters[right_int] += 1
        else:
            right_counters[right_int] = 1

    res = []
    for i in range(len(left_arr)):
        res.append(left_arr[i] * right_counters.get(left_arr[i], 0))

    print(f'Part 2: {sum(res)}')


if __name__ == "__main__":
    part1()
    part2()
