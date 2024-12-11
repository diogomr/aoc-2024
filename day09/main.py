def part1():
    input = list(map(int, open('input.txt').read().splitlines()[0]))

    cur_pos = 0
    files = []
    spaces = []
    for i in range(len(input)):
        for x in range(cur_pos, cur_pos + input[i]):
            if i % 2 == 0:
                files.append((x, i // 2))
            else:
                spaces.append(x)

        cur_pos += input[i]

    backwards = -1
    for s in spaces:
        pos, id = files[backwards]
        if s > pos:
            break

        files[backwards] = (s, id)
        backwards -= 1

    res = 0
    for pos, id in files:
        res += pos * id

    return res


def part2():
    input = list(map(int, open('input.txt').read().splitlines()[0]))

    cur_pos = 0
    files = []
    spaces = []
    for i in range(len(input)):
        if i % 2 == 0:
            files.append(((cur_pos, cur_pos + input[i] - 1), i // 2))
        else:
            spaces.append((cur_pos, cur_pos + input[i] - 1))
        cur_pos += input[i]

    for f_idx in reversed(range(len(files))):
        for s_idx in range(len(spaces)):
            if spaces[s_idx][0] > files[f_idx][0][0]:
                break

            space_size = spaces[s_idx][1] - spaces[s_idx][0] + 1
            file_size = files[f_idx][0][1] - files[f_idx][0][0] + 1

            if space_size < file_size:
                continue
            elif space_size > file_size:
                start = spaces[s_idx][0]
                end = spaces[s_idx][0] + file_size - 1

                spaces[s_idx] = (end + 1, spaces[s_idx][1])
                files[f_idx] = ((start, end), files[f_idx][1])
                break
            else:
                files[f_idx] = ((spaces[s_idx][0], spaces[s_idx][1]), files[f_idx][1])
                del spaces[s_idx]
                break

    res = 0
    for (start_p, end_p), id in sorted(files):
        for pos in range(start_p, end_p + 1):
            res += pos * id

    return res


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
