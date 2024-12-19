import heapq
import textwrap
import re


def part1(input: str):
    (parts, goals) = parse_input(input)
    possible = 0
    for goal in goals:
        if is_possible(goal, parts):
            possible += 1
    return possible

def part2(input: str, w, h):
    return 0

def parse_input(input: str):
    lines = input.splitlines()
    parts = set(lines[0].split(", "))
    goals = lines[2:]
    return (parts, goals)

def is_possible(goal, parts):
    if goal == '':
        return True
    for part in parts:
        if goal.startswith(part):
            if is_possible(goal[len(part):], parts):
                return True
    return False

if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    r, wr, b, g, bwu, rb, gb, br

    brwrr
    bggr
    gbbr
    rrbgbr
    ubwu
    bwurrg
    brgr
    bbrgwb
    """).strip()
    input = open("day19.txt").read()
    print(f"Part 1 test, 6 expected: {part1(test_input1)}")
    print(f"Part 1: {part1(input)}")

