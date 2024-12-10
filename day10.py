import textwrap

def part1(input: str):
    sum = 0
    data = parse_input(input)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                sum += trailhead_score(data, y, x)
    return sum

def part2(input: str):
    sum = 0
    data = parse_input(input)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                sum += trailhead_rating(data, y, x)
    return sum

def parse_input(input: str):
    result = []
    for line in input.splitlines():
        result.append([])
        for char in line:
            result[-1].append(int(char))
    return result

def trailhead_score(data, y, x):
    ends = set()
    stack = [(y, x)]
    while stack:
        pos = stack.pop()
        height = data[pos[0]][pos[1]]
        if height == 9:
            ends.add(pos)
            continue
        for n in neighbors(data, pos[0], pos[1]):
            if data[n[0]][n[1]] == height + 1:
                stack.append((n[0], n[1]))
    return len(ends)

def trailhead_rating(data, y, x):
    result = 0
    stack = [(y, x)]
    while stack:
        pos = stack.pop()
        height = data[pos[0]][pos[1]]
        if height == 9:
            result += 1
            continue
        for n in neighbors(data, pos[0], pos[1]):
            if data[n[0]][n[1]] == height + 1:
                stack.append((n[0], n[1]))
    return result

def neighbors(data, y, x):
    candidates = [
        (y - 1, x),
        (y, x + 1),
        (y + 1, x),
        (y, x - 1),
    ]
    return [c for c in candidates if c[0] >= 0 and c[0] < len(data) and c[1] >= 0 and c[1] < len(data[0])]

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    89010123
    78121874
    87430965
    96549874
    45678903
    32019012
    01329801
    10456732
    """).strip()
    input = open('day10.txt').read()
    print(f"Part 1 test, 36 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")

    print(f"Part 2 test, 81 expected: {part2(test_input)}")
    print(f"Part 2: {part2(input)}")
