import textwrap

def part1(input: str) -> int:
    lines = input.strip().splitlines()

    def matches_at(needle: str, y: int, x: int) -> int:
        def is_match(dy, dx) -> bool:
            for i in range(len(needle)):
                ty = y + i * dy
                tx = x + i * dx
                if ty < 0 or tx < 0 or ty >= len(lines) or tx >= len(lines[ty]):
                    return False
                if lines[ty][tx] != needle[i]:
                    return False
            return True

        matches = 0
        for (dy, dx) in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
            if is_match(dy, dx):
                matches += 1
        return matches


    matches_total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            matches_total += matches_at( "XMAS", y, x)
    return matches_total


def part2(input: str) -> int:
    lines = input.strip().splitlines()

    def matches_at(y: int, x: int) -> int:
        def is_match(variant) -> bool:
            needle = "MAS"
            for (i, (dy, dx)) in enumerate(variant):
                iy = y + dy
                ix = x + dx
                if iy < 0 or ix < 0 or iy >= len(lines) or ix >= len(lines[y]):
                    return False
                if lines[iy][ix] != needle[i]:
                    return False
            return True

        variants = [
            (((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2))),
            (((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))),
            (((2,2),(1,1),(0,0)),((2,0),(1,1),(0,2))),
            (((2,2),(1,1),(0,0)),((0,2),(1,1),(2,0))),
        ]
        matches = 0
        for (first, second) in variants:
            if is_match(first) and is_match(second):
                matches += 1
        return matches

    matches_total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            matches_total += matches_at( y, x)
    return matches_total

if __name__ == "__main__":
    test_input = textwrap.dedent("""
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    """).strip()
    input = open("day4.txt", 'r').read()

    print("Part 1 test, expected 18: %s" % part1(test_input))
    print("Part 1: %s" % part1(input))

    print("Part 2 test, expected 9: %s" % part2(test_input))
    print("Part 2: %s" % part2(input))
