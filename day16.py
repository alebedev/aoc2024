import textwrap

def part1(input: str):
    maze = parse_input(input)
    best_score = find_paths(maze)
    best_result = min((best_score[key] for key in best_score if key[0] == maze['target']))
    return best_result

def part2(input: str):
    maze = parse_input(input)
    best_score = find_paths(maze)
    best_result = min((best_score[key] for key in best_score if key[0] == maze['target']))
    walk_back_states = [(state, score) for state, score in best_score.items() if state[0] == maze['target'] and score == best_result]
    visited = set()
    while walk_back_states:
        (state, score) = walk_back_states.pop()

        if state in visited:
            continue
        visited.add(state)

        (pos, h_index) = state
        if pos == maze['start']:
            continue

        heading = HEADINGS[h_index]
        possible_prev_states = [
            # back
            (((pos[0] - heading[0], pos[1] - heading[1]), h_index), score - 1),
            # turn left
            ((pos, h_index - 1 if h_index > 0 else len(HEADINGS) - 1), score - 1000),
            # turn right
            ((pos, h_index + 1 if h_index + 1 < len(HEADINGS) else 0), score - 1000),
        ]
        for prev in possible_prev_states:
            if prev[0] in best_score and prev[1] == best_score[prev[0]]:
                walk_back_states.append(prev)
    seats = set(pos for (pos, h_index) in visited)
    return len(seats)

def find_paths(maze):
    stack = [(maze['start'], maze['heading'], 0)]
    best_score = {}
    while stack:
        step = stack.pop(0)
        (pos, h_index, cur_score) = step
        heading = HEADINGS[h_index]

        if (pos, h_index) in best_score:
            old_best_score = best_score[(pos, h_index)]
            if cur_score >= old_best_score:
                continue

        best_score[(pos, h_index)] = cur_score

        # step forward
        next = (pos[0] + heading[0], pos[1] + heading[1])
        if next[0] > 0 and next[0] < maze['width'] and next[1] > 0 and next[1] < maze['height']:
            if next not in maze['walls']:
                stack.append((next, h_index, cur_score + 1))
        # rotate left
        next_h_index = len(HEADINGS) - 1 if h_index - 1 < 0 else h_index - 1
        stack.append((pos, next_h_index, cur_score + 1000))
        # rotate right
        next_h_index = h_index + 1 if h_index + 1 < len(HEADINGS) else 0
        stack.append((pos, next_h_index, cur_score + 1000))
    return best_score

HEADINGS = [
    (0, -1), # top
    (1, 0), # right
    (0, 1), # bottom
    (-1, 0), # left
]

def parse_input(input: str):
    walls = set()
    start = None
    target = None
    for (y, line) in enumerate(input.splitlines()):
        for (x, char) in enumerate(line):
            match char:
                case 'E':
                    target = (x, y)
                case 'S':
                    start = (x, y)
                case '#':
                    walls.add((x, y))
                case '.':
                    pass
                case _:
                    raise Exception(f"Unknown character {char}")
    return {
        'walls': walls,
        'start': start,
        'target': target,
        'width': x + 1,
        'height': y + 1,
        'heading': 1
    }



if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    ###############
    #.......#....E#
    #.#.###.#.###.#
    #.....#.#...#.#
    #.###.#####.#.#
    #.#.#.......#.#
    #.#.#####.###.#
    #...........#.#
    ###.#.#####.#.#
    #...#.....#.#.#
    #.#.#.###.#.#.#
    #.....#...#.#.#
    #.###.#.#.#.#.#
    #S..#.....#...#
    ###############
    """).strip()
    test_input2 = textwrap.dedent("""
    #################
    #...#...#...#..E#
    #.#.#.#.#.#.#.#.#
    #.#.#.#...#...#.#
    #.#.#.#.###.#.#.#
    #...#.#.#.....#.#
    #.#.#.#.#.#####.#
    #.#...#.#.#.....#
    #.#.#####.#.###.#
    #.#.#.......#...#
    #.#.###.#####.###
    #.#.#...#.....#.#
    #.#.#.#####.###.#
    #.#.#.........#.#
    #.#.#.#########.#
    #S#.............#
    #################
    """).strip()
    input = open("day16.txt").read()
    print(f"Part 1 test, 7036 expected: {part1(test_input1)}")
    print(f"Part 1 test, 11048 expected: {part1(test_input2)}")
    print(f"Part 1: {part1(input)}")

    print(f"Part 2 test, 45 expected: {part2(test_input1)}")
    print(f"Part 2 test, 64 expected: {part2(test_input2)}")
    print(f"Part 2: {part2(input)}")
