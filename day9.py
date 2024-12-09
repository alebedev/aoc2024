import textwrap

def part1(input: str):
    compressed = compress(parse_input(input))
    return checksum(compressed)

def part2(input: str):
    return 0

def parse_input(input: str):
    result = []
    id = 0
    for (i,char) in enumerate(input):
        assert char.isdigit()
        size = int(char)
        for j in range(size):
            if i % 2 == 0:
                result.append(id)
            else:
                result.append(None)
        if i % 2 == 0:
            id += 1
    return result

def compress(list):
    result = list.copy()
    i = 0
    j = len(list) - 1
    while i < j:
        if result[i] != None:
            i += 1
        elif result[j] != None:
            result[i] = result[j]
            result[j] = None
            j -= 1
        else:
            j -= 1
    return result

def checksum(list):
    sum = 0
    for (i,x) in enumerate(list):
        if x != None:
            sum += i * x
    return sum

if __name__ == "__main__":
    test_input = "2333133121414131402"
    input = open('day9.txt').read()
    print(f"Part 1 test, 1928 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")

    # print(f"Part 2 test, ? expected: {part2(test_input)}")
    # print(f"Part 2: {part2(input)}")