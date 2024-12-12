import textwrap

def part1(input: str) -> int:
    grid = parse_input(input)
    plots = by_plots(grid)
    # print(plots)
    sum = 0
    for p in plots:
        sum += plot_score(p)
    return sum

def part2(input: str) -> int:
    grid = parse_input(input)
    plots = by_plots(grid)
    # print(plots)
    sum = 0
    for p in plots:
        sum += plot_score2(p, grid)
    return sum

def parse_input(input: str):
    return [
        [c for c in line]
        for line in input.splitlines()
    ]

def by_plots(grid):
    result = []
    visited = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (y, x) in visited:
                continue
            plot = plot_from(grid, y, x)
            visited = visited.union(set(plot))
            result.append(plot)
    return result

def plot_from(grid, y, x):
    stack = [(y,x)]
    visited = set()
    char = grid[y][x]
    while len(stack) > 0:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for (y,x) in neighbors(grid, cur[0], cur[1]):
            if grid[y][x] == char:
                stack.append((y,x))
    return list(visited)

def neighbors(grid, y, x):
    result = []
    if y < len(grid) - 1:
        result.append((y + 1, x))
    if x < len(grid[0]) - 1:
        result.append((y, x + 1))
    if y > 0:
        result.append((y - 1, x))
    if x > 0:
        result.append((y, x - 1))
    return result

def plot_score(plot):
    cells = set(plot)
    area = 0
    perimeter = 0
    for pos in plot:
        area += 1
        perimeter += 4
        if (pos[0] - 1, pos[1]) in cells:
            perimeter -= 1
        if (pos[0], pos[1] - 1) in cells:
            perimeter -= 1
        if (pos[0] + 1, pos[1]) in cells:
                perimeter -= 1
        if (pos[0], pos[1] + 1) in cells:
                perimeter -= 1
    return area * perimeter

def plot_score2(plot, grid):
    cells = set(plot)
    area = 0
    sides = 0
    for pos in plot:
        area += 1
    print(plot, area, sides)
    return area * sides

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    AAAA
    BBCD
    BBCC
    EEEC
    """).strip()
    test_input2 = textwrap.dedent("""
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
    """).strip()
    test_input3 = textwrap.dedent("""
    OOOOO
    OXOXO
    OOOOO
    OXOXO
    OOOOO
    """).strip()
    input = open("day12.txt").read()
    print(f"Part 1 test, 140 expected: {part1(test_input)}")
    print(f"Part 1 test 2, 1930 expected: {part1(test_input2)}")
    print(f"Part 1 test 3, 772 expected: {part1(test_input3)}")
    print(f"Part 1: {part1(input)}")
    #
    print(f"Part 2 test, 80 expected: {part2(test_input)}")
    # print(f"Part 2: {part2(input)}")
