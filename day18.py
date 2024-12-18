import textwrap
import re


def part1(input: str, w, h, walls_count):
    walls = set(parse_input(input)[:walls_count])
    maze = {
        'walls': walls,
        'width': w,
        'height': h,
        'start': (0, 0),
        'target': (w - 1, h - 1),
    }
    return find_paths(maze)


def part2(input: str):
    return 0


def parse_input(input: str):
    result = []
    for line in input.splitlines():
        (x, y) = line.split(',')
        result.append((int(x), int(y)))
    return result


def find_paths(maze):
    costs = {
        maze['start']: 0
    }
    queue = [(maze['start'], 0)]
    while queue:
        (pos, cost) = queue.pop()
        for n in neighbors(maze, pos):
            if n in costs:
                if costs[n] <= cost + 1:
                    continue
            costs[n] = cost + 1
            queue.append((n, cost + 1))
    return costs[maze['target']]


def neighbors(maze, pos):
    return [
        n for n in [
            (pos[0] - 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
            (pos[0] + 1, pos[1]),
        ]
        if n[0] >= 0 and n[0] < maze['width'] and n[1] >= 0 and n[1] < maze['height'] and n not in maze['walls']
    ]


if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    5,4
    4,2
    4,5
    3,0
    2,1
    6,3
    2,4
    1,5
    0,6
    3,3
    2,6
    5,1
    1,2
    5,5
    2,5
    6,5
    1,4
    0,4
    6,4
    1,1
    6,1
    1,0
    0,5
    1,6
    2,0
    """).strip()
    input = open("day18.txt").read()
    print(f"Part 1 test, 22 expected: {part1(test_input1, w=7, h=7, walls_count=12)}")
    print(f"Part 1: {part1(input, w=71, h=71, walls_count=1024)}")
