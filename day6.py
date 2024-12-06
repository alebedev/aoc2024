import copy
import textwrap

def part1(input: str) -> int:
    (maze, pos) = parse(input)
    visited = { pos }
    directions = (
        (-1, 0), (0, 1), (1, 0), (0, -1)
    )
    dir_i = 0
    while True:
        direction = directions[dir_i]
        next = (pos[0] + direction[0], pos[1] + direction[1])
        if next[0] >= len(maze) or next[1] >= len(maze[0]):
            return len(visited)
        if maze[next[0]][next[1]] == '#':
            dir_i += 1
            if dir_i >= len(directions):
                dir_i = 0
        else:
            pos = next
            visited.add(pos)

def part2(input: str) -> int:
    (maze, start_pos) = parse(input)
    directions = (
        (-1, 0), (0, 1), (1, 0), (0, -1)
    )
    def full_path(maze, start_pos, dir_i):
        pos = start_pos
        visited = set()
        while True:
            visited.add((pos, dir_i))
            direction = directions[dir_i]
            next = (pos[0] + direction[0], pos[1] + direction[1])
            if next[0] >= len(maze) or next[0] < 0 or next[1] >= len(maze[0]) or next[1] < 0:
                return {
                    "path": visited,
                    "is_loop": False
                }
            if (next, dir_i) in visited:
                return {
                    "path": visited,
                    "is_loop": True
                }
            if maze[next[0]][next[1]] == '#':
                dir_i += 1
                if dir_i >= len(directions):
                    dir_i = 0
            else:
                pos = next

    # fills potential_loops
    all_visited = full_path(maze, start_pos, 0)["path"]
    # print("Potential loops:", len(all_visited))

    loops = set()
    for (pos, dir_i) in all_visited:
        if pos == start_pos:
            continue
        maze_with_block = copy.deepcopy(maze)
        maze_with_block[pos[0]][pos[1]] = '#'
        if full_path(maze_with_block, start_pos, 0)["is_loop"]:
            # print(f"Loop detected {pos}, {direction}")
            loops.add(pos)
        # sys.stdout.write(".")
    return len(loops)

def parse(input: str):
    lines = input.splitlines()
    result = []
    start = None
    for (y, line) in enumerate(lines):
        result.append([])
        for (x, char) in enumerate(line):
            if char == "^":
                start = (y, x)
                result[y].append(".")
            else:
                result[y].append(char)
    return (result, start)

if __name__ == "__main__":
    test_input = textwrap.dedent("""
        ....#.....
        .........#
        ..........
        ..#.......
        .......#..
        ..........
        .#..^.....
        ........#.
        #.........
        ......#...
        """
    ).strip()
    input = open('day6.txt').read()

    print("Part 1 test, 41 expected: %s" % part1(test_input))
    print("Part 1: %s" % part1(input))

    print("Part 2 test, 6 expected: %s" % part2(test_input))
    # print("Part 2 time (100x): %s" % timeit.timeit(lambda: part2(test_input), number=100))
    print("Part 2: %s" % part2(input))
