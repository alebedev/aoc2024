import textwrap

def part1(input: str, iterations: int) -> int:
    stones = parse_input(input)
    for i in range(iterations):
        stones = step(stones)
        # print(stones)
    return len(stones)

def part2(input: str):
    pass

def step(stones):
    result = []
    for stone in stones:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            a = int(s[:len(s) // 2])
            b = int(s[len(s) // 2:])
            result.append(a)
            result.append(b)
        else:
            result.append(2024 * stone)
    return result

def parse_input(input: str):
    return [int(x) for x in input.split(" ")]

if __name__ == "__main__":
    test_input = "125 17"
    # input = open('day11.txt').read()
    print(f"Part 1 test, 55312 expected: {part1(test_input, 25)}")
    print(f"Part 1: {part1("814 1183689 0 1 766231 4091 93836 46", 25)}")

    # print(f"Part 2 test, 81 expected: {part2(test_input)}")
    # print(f"Part 2: {part2(input)}")
