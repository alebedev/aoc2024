from itertools import groupby


def part1():
    data = open('./day1.txt', 'r').read().splitlines()
    pairs = [x.split() for x in data]
    a = sorted([int(x[0]) for x in pairs])
    b = sorted([int(x[1]) for x in pairs])
    diff = 0
    for i in range(len(a)):
        diff = diff + abs(a[i] - b[i])
    print(diff)

def part2():
    data = open('./day1.txt', 'r').read().splitlines()
    pairs = [x.split() for x in data]
    a = {key: len(list(group)) for key, group in groupby(sorted([int(x[0]) for x in pairs]))}
    b = {key: len(list(group)) for key, group in groupby(sorted([int(x[1]) for x in pairs]))}
    score = 0
    for key, size in a.items():
        score += key * size * b.get(key, 0)
    print(score)

if __name__ == '__main__':
    part1()
    part2()