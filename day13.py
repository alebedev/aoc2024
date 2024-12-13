import re
import textwrap
from json.encoder import INFINITY


def part1(input: str) -> int:
    problems = parse_input(input)
    total_cost = 0
    for problem in problems:
        total_cost += cost_to_solve(problem['prize'], problem['a'], problem['b'])
    return total_cost

def part2(input: str) -> int:
    return 0

def parse_input(input: str):
    result = []
    for problem_text in input.split("\n\n"):
        [(x, y)] = re.findall(r"Button A: X\+(?P<x>\d+), Y\+(?P<y>\d+)", problem_text)
        a = (int(x), int(y))
        [(x, y)] = re.findall(r"Button B: X\+(?P<x>\d+), Y\+(?P<y>\d+)", problem_text)
        b = (int(x), int(y))
        [(x, y)] = re.findall(r"Prize: X=(?P<x>\d+), Y=(?P<y>\d+)", problem_text)
        prize = (int(x), int(y))
        result.append({'a': a, 'b': b, 'prize': prize})
    return result

def cost_to_solve(target, a, b):
    costs = {}
    # a_slope = a[0] / a[1]
    # b_slope = b[0] / b[1]
    # target_slope = target[0] / target[1]
    # print(target, a_slope, b_slope, target_slope)
    costs[(0,0)] = 0
    queue = [((0, 0), (0, 0))]
    while queue:
        (pos, steps) = queue.pop(0)
        # print(pos, step)
        if steps[0] >= 100 or steps[1] >= 100:
            continue
        elif pos == target:
            return costs[pos]
        elif pos[0] > target[0] or pos[1] > target[1]:
            continue
        next_a = (pos[0] + a[0], pos[1] + a[1])
        best_cost_a = costs.get(next_a, float('inf'))
        cost_a = costs[pos] + 3
        if cost_a < best_cost_a:
            costs[next_a] = cost_a
            queue.append((next_a, (steps[0] + 1, steps[1])))
        next_b = (pos[0] + b[0], pos[1] + b[1])
        best_cost_b = costs.get(next_b, float('inf'))
        cost_b = costs[pos] + 1
        if cost_b < best_cost_b:
            costs[next_b] = cost_b
            queue.append((next_b, (steps[0], steps[1] + 1)))
    return costs.get(target, 0)

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    
    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176
    
    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450
    
    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279
    """).strip()
    input = open("day13.txt").read()
    print(f"Part 1 test, 480 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")
    #
    # print(f"Part 2 test, 80 expected: {part2(test_input)}")
    # print(f"Part 2: {part2(input)}")
