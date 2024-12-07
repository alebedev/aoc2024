import textwrap

def part1(input: str):
    data = parse_input(input)
    sum_valid = 0
    for line in data:
        if valid_total(line["result"], line["parts"]):
            sum_valid += line["result"]
    return sum_valid

def part2(input: str):
    data = parse_input(input)
    sum_valid = 0
    for line in data:
        if valid_total(line["result"], line["parts"], allow_concat=True):
            sum_valid += line["result"]
    return sum_valid

def parse_input(input: str):
    lines = []
    for line in input.splitlines():
        (result, parts) = line.split(": ")
        lines.append({
            "result": int(result),
            "parts": [int(x) for x in parts.split(" ")]
        })
    return lines

def valid_total(sum, parts, allow_concat=False):
    variants = [(0, parts)]
    while len(variants) > 0:
        (result, items) = variants.pop()
        if len(items) == 0:
            if result == sum:
                return True
            else:
                continue
        item, rest = items[0], items[1:]
        if result > sum:
            continue
        if result > 0:
            variants.append((result * item, rest))
            if allow_concat:
                variants.append((int(f"{result}{item}"), rest))
        variants.append((result + item, rest))
    return False

if __name__ == "__main__":
    test_input = textwrap.dedent("""
    190: 10 19
    3267: 81 40 27
    83: 17 5
    156: 15 6
    7290: 6 8 6 15
    161011: 16 10 13
    192: 17 8 14
    21037: 9 7 18 13
    292: 11 6 16 20
    """).strip()
    input = open('day7.txt').read()
    print(f"Part 1 test, 3749 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2 test, 11387 expected {part2(test_input)}")
    print(f"Part 2: {part2(input)}")