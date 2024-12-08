import textwrap

def part1(input: str):
    data = parse_input(input)
    antinodes = set()
    for (char, emitters) in data['emitters'].items():
        for i in range(len(emitters)):
            for j in range(i + 1, len(emitters)):
                antinodes.add(antinode_for(emitters[i], emitters[j]))
                antinodes.add(antinode_for(emitters[j], emitters[i]))
    for candidate in antinodes.copy():
        if not in_range(candidate, data['height'], data['width']):
            antinodes.remove(candidate)
    return len(antinodes)

def part2(input: str):
    data = parse_input(input)
    antinodes = set()
    for (char, emitters) in data['emitters'].items():
        for i in range(len(emitters)):
            for j in range(i + 1, len(emitters)):
                for pos in antinodes_for(emitters[i], emitters[j], data['height'], data['width']):
                    antinodes.add(pos)
                for pos in antinodes_for(emitters[j], emitters[i], data['height'], data['width']):
                    antinodes.add(pos)
    return len(antinodes)

def parse_input(input: str):
    emitters = {}
    for (y, line) in enumerate(input.splitlines()):
        for (x, char) in enumerate(line):
            if char == '.':
                continue
            if char not in emitters:
                emitters[char] = []
            emitters[char].append((y, x))
    return {
        'emitters': emitters,
        'height': len(input.splitlines()),
        'width': len(input.splitlines()[0])
    }

def antinode_for(a, b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    return (a[0] + dy, a[1] + dx)

def antinodes_for(a, b, height, width):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    result = []
    next = a
    while True:
        if in_range(next, height, width):
            result.append(next)
        else: break
        next = (next[0] + dy, next[1] + dx)
    return result

def in_range(pos, height, width):
    return pos[0] >= 0 and pos[0] < height and pos[1] >= 0 and pos[1] < width

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    ............
    ........0...
    .....0......
    .......0....
    ....0.......
    ......A.....
    ............
    ............
    ........A...
    .........A..
    ............
    ............
    """).strip()
    input = open('day8.txt').read()
    print(f"Part 1 test, 14 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")

    part2_test2 = textwrap.dedent("""
    T.........
    ...T......
    .T........
    ..........
    ..........
    ..........
    ..........
    ..........
    ..........
    ..........
    """).strip()
    print(f"Part 2 test, 34 expected: {part2(test_input)}")
    print(f"Part 2 test, 9 expected: {part2(part2_test2)}")
    print(f"Part 2: {part2(input)}")