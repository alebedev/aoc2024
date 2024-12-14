import re
import textwrap
from json.encoder import INFINITY


def part1(input: str, w: int, h: int) -> int:
    data = parse_input(input)
    step = data
    for i in range(100):
        step = simulate(step, w, h)
    # print(f"Post-steps: {[x[0] for x in step]}")
    return score(step, w, h)

def part2(input: str) -> int:
    return 0

def parse_input(input: str):
    result = []
    for line in input.splitlines():
        m = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)
        if m:
            groups = m.groups()
            result.append(((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3]))))
    return result

def simulate(data, w, h):
    result = []
    for robot in data:
        (pos, vel) = robot
        result.append((move(pos, vel, w, h), vel))
    return result

def move(pos, vel, w, h):
    x = pos[0] + vel[0]
    y = pos[1] + vel[1]
    if x < 0:
        x = w + x
    elif x >= w:
        x = x - w
    if y < 0:
        y = h + y
    elif y >= h:
        y = y - h
    return (x, y)

def score(data, w,  h):
    assert w % 2 == 1
    assert h % 2 == 1
    med_w = (w // 2)
    med_h = (h // 2)
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (pos, vel) in data:
        (x, y) = pos
        if x < med_w and y < med_h:
            q1 += 1
        elif x > med_w and y < med_h:
            q2 += 1
        elif x < med_w and y > med_h:
            q3 += 1
        elif x > med_w and y > med_h:
            q4 += 1
    return q1 * q2 * q3 * q4

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    p=0,4 v=3,-3
    p=6,3 v=-1,-3
    p=10,3 v=-1,2
    p=2,0 v=2,-1
    p=0,0 v=1,3
    p=3,0 v=-2,-2
    p=7,6 v=-1,-3
    p=3,0 v=-1,-2
    p=9,3 v=2,3
    p=7,3 v=-1,2
    p=2,4 v=2,-3
    p=9,5 v=-3,-3
    """).strip()
    input = open("day14.txt").read()
    print(f"Part 1 test, 12 expected: {part1(test_input, w=11, h=7)}")
    print(f"Part 1: {part1(input, w=101, h=103)}")
    #
    # print(f"Part 2 test, ? expected: {part2(test_input)}")
    # print(f"Part 2: {part2(input)}")
