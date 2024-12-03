import re


def part1(input: str) -> int:
    """
    >>> part1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    161
    """
    sum = 0
    for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input, re.MULTILINE):
        sum += int(match[0]) * int(match[1])
    return sum

def part2(input: str) -> int:
    """
    >>> part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    48
    """
    sum = 0
    enabled = True
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input, re.MULTILINE):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            (a, b) = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", match).groups()
            sum += int(a) * int(b)

    return sum

if __name__ == '__main__':
    with open('day3.txt', 'r') as file:
        input = file.read()
    print(part1(input))
    print(part2(input))
