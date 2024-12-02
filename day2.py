def part1():
    data = open('day2.txt').read().splitlines()
    safe_lines = 0
    for line in data:
        levels = [int(x) for x in line.split()]
        first = levels.pop(0)
        increasing = levels[0] > first
        safe = True
        while len(levels) > 0:
            next = levels.pop(0)
            diff = abs(first - next)
            if diff < 1 or diff > 3:
                safe = False
                break
            if increasing and first > next:
                safe = False
                break
            if (not increasing) and first < next:
                safe = False
                break
            first = next
        if (safe):
            safe_lines += 1
    print(safe_lines)

if __name__ == '__main__':
    part1()
