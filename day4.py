import textwrap

def part1(input: str) -> int:
    lines = input.strip().splitlines()
    matches_total = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            matches_total += matches_at(lines, "XMAS", y, x)
    return matches_total

def matches_at(lines: list[str], needle: str, y: int, x: int) -> int:
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

if __name__ == "__main__":
    print("Test, expected 18: %s" % part1(textwrap.dedent("""
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
    """).strip()))
    input = open("day4.txt", 'r').read()
    print("Part 1: %s" % part1(input))
