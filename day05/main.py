def is_valid(update, rules):
    for i in range(len(update)):
        before = update[i]
        after = rules.get(before)
        if after is None:
            continue

        for elem in after:
            if elem in update and update.index(elem) < i:
                return False, (i, update.index(elem))

    return True, None


def part1():
    rules_input, updates_input = open('input.txt').read().split("\n\n")
    rules_input = rules_input.splitlines()
    updates_input = updates_input.splitlines()

    rules = {}
    for rule in rules_input:
        a, b = map(int, rule.split("|"))
        if rules.get(a) is None:
            rules[a] = [b]
        else:
            rules[a].append(b)

    updates = []
    for update in updates_input:
        updates.append(list(map(int, update.split(","))))

    valid_updates = []
    for update in updates:
        valid, _ = is_valid(update, rules)
        if valid:
            valid_updates.append(update)

    ans = 0
    for update in valid_updates:
        idx = len(update) // 2
        ans += update[idx]

    return ans


def part2():
    rules_input, updates_input = open('input.txt').read().split("\n\n")
    rules_input = rules_input.splitlines()
    updates_input = updates_input.splitlines()

    rules = {}
    for rule in rules_input:
        a, b = map(int, rule.split("|"))
        if rules.get(a) is None:
            rules[a] = [b]
        else:
            rules[a].append(b)

    updates = []
    for update in updates_input:
        updates.append(list(map(int, update.split(","))))

    invalid_updates = []
    for update in updates:
        valid, _ = is_valid(update, rules)
        if not valid:
            invalid_updates.append(update)

    for update in invalid_updates:
        while True:
            valid, swap = is_valid(update, rules)
            if valid:
                break
            a, b = swap
            temp = update[a]
            update[a] = update[b]
            update[b] = temp

    ans = 0
    for update in invalid_updates:
        idx = len(update) // 2
        ans += update[idx]

    return ans


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
