def part1():
    data = open('day2.txt').read().splitlines()
    safe_lines = 0
    for line in data:
        levels = [int(x) for x in line.split()]
        if is_safe(levels.copy()):
            safe_lines += 1
    return safe_lines

def is_safe(levels):
    copy = levels.copy()
    first = copy.pop(0)
    increasing = copy[0] > first
    while len(copy) > 0:
        next = copy.pop(0)
        diff = abs(first - next)
        if diff < 1 or diff > 3:
            return False
        if increasing and first > next:
            return False
        if (not increasing) and first < next:
            return False
        first = next
    return True

def part2():
    data = open('day2.txt').read().splitlines()
    safe_lines = 0
    for line in data:
        levels = [int(x) for x in line.split()]
        if is_safe(levels.copy()):
            safe_lines += 1
        else:
            for i in range(0, len(levels)):
                modified = levels.copy()
                modified.pop(i)
                if is_safe(modified):
                    safe_lines += 1
                    break
    return safe_lines



if __name__ == '__main__':
    print(part1())
    print(part2())
