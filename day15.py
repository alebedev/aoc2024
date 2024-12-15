import copy
import sys
import textwrap

def part1(input: str):
    (state, moves) = parse_input(input)
    for move in moves:
        state = run_move(state, move)
        # print_state(state)
    # print(f"Final state:")
    # print_state(state)
    return boxes_score(state)

def part2(input: str):
    return None

def parse_input(input: str):
    def parse_state(state_str: str):
        walls = set()
        boxes = set()
        robot = None
        for (y, line) in enumerate(state_str.splitlines()):
            for (x, char) in enumerate(line):
                if char == "#":
                    walls.add((x, y))
                elif char == ".":
                    continue
                elif char == "O":
                    boxes.add((x, y))
                elif char == "@":
                    robot = (x, y)
                else:
                    raise Exception(f"Unknown character {char}")
        return {
            'walls': walls,
            'boxes': boxes,
            'robot': robot,
            'width': x + 1,
            'height': y + 1,
        }

    def parse_moves(move_str: str):
        result = []
        for char in move_str:
            match char:
                case '<':
                    result.append((-1, 0))
                case '^':
                    result.append((0, -1))
                case '>':
                    result.append((1, 0))
                case 'v':
                    result.append((0, 1))
                case '\n':
                    continue
                case _:
                    raise Exception(f"Unknown character {char}")
        return result

    [state_str, moves_str] = input.split("\n\n")
    state = parse_state(state_str)
    moves = parse_moves(moves_str)
    return (state, moves)

def run_move(state, move):
    result = copy.deepcopy(state)
    next = (state['robot'][0] + move[0], state['robot'][1] + move[1])
    if next in state['walls']:
        return result
    if next in state['boxes']:
        result['boxes'] = move_box(state, next, move)
    if next not in result['boxes']:
        result['robot'] = next
    return result

def move_box(state, next, move):
    boxes = state['boxes'].copy()
    target = (next[0] + move[0], next[1] + move[1])
    if target in state['walls']:
        return boxes
    if target in state['boxes']:
        boxes = move_box(state, target, move)
    if target not in boxes:
        boxes.remove(next)
        boxes.add(target)
    return boxes

def print_state(state):
    for y in range(state['height']):
        for x in range(state['width']):
            if (x, y) == state['robot']:
                sys.stdout.write("@")
            elif (x, y) in state['walls']:
                sys.stdout.write("#")
            elif (x, y) in state['boxes']:
                sys.stdout.write("O")
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")

def boxes_score(state):
    score = 0
    for box in state['boxes']:
        score += box[0] + 100 * box[1]
    return score

if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    ########
    #..O.O.#
    ##@.O..#
    #...O..#
    #.#.O..#
    #...O..#
    #......#
    ########
    
    <^^>>>vv<v>>v<<
    """).strip()
    test_input2 = textwrap.dedent("""
    ##########
    #..O..O.O#
    #......O.#
    #.OO..O.O#
    #..O@..O.#
    #O#..O...#
    #O..O..O.#
    #.OO.O.OO#
    #....O...#
    ##########
    
    <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
    vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
    ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
    <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
    ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
    ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
    >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
    <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
    ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
    v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    """).strip()
    input = open("day15.txt").read()
    print(f"Part 1 test, 2028 expected: {part1(test_input1)}")
    print(f"Part 1 test, 10092 expected: {part1(test_input2)}")
    print(f"Part 1: {part1(input)}")
