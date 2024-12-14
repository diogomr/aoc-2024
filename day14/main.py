import re
from dataclasses import dataclass


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def part1():
    input = open('input.txt').read().splitlines()

    w = 101
    h = 103

    robots = []
    for line in input:
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(Robot(x=int(match[1]), y=int(match[2]), vx=int(match[3]), vy=int(match[4])))

    for _ in range(100):
        for robot in robots:
            robot.x = (robot.x + robot.vx) % w
            robot.y = (robot.y + robot.vy) % h

    mw = w // 2
    mh = h // 2

    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        if robot.x < mw and robot.y < mh:
            q1 += 1
        elif robot.x > mw and robot.y < mh:
            q2 += 1
        elif robot.x < mw and robot.y > mh:
            q3 += 1
        elif robot.x > mw and robot.y > mh:
            q4 += 1

    return q1 * q2 * q3 * q4


def part2():
    input = open('input.txt').read().splitlines()

    w = 101
    h = 103

    robots = []
    for line in input:
        match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(Robot(x=int(match[1]), y=int(match[2]), vx=int(match[3]), vy=int(match[4])))

    seconds = 1
    while True:
        robots_pos = {}
        for robot in robots:
            robot.x = (robot.x + robot.vx) % w
            robot.y = (robot.y + robot.vy) % h
            robots_pos[(robot.x, robot.y)] = True

        map = ""
        for x in range(w):
            for y in range(h):
                if robots_pos.get((x, y)) != None:
                    map += "#"
                else:
                    map += " "
            map += "\n"

        if "##########" in map:
            print(f"Seconds: #{seconds}")
            print(map)
            print()
            print()
            print()
            break

        seconds += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
