import textwrap

def part1(input: str):
    pairs = parse_input(input)
    triplets = find_triplets(pairs)
    sum = 0
    for triplet in triplets:
        for item in triplet:
            if item.startswith('t'):
                sum += 1
                break
    return sum

def part2(input: str):
    return 0

def parse_input(input: str):
    pairs = [
        (line.split("-")[0], line.split("-")[1])
        for line in input.splitlines()
    ]
    return pairs

def find_triplets(pairs):
    # Union-find would be more efficient
    connections = {}
    def add_connection(a, b):
        if a not in connections:
            connections[a] = set()
        connections[a].add(b)
        if b not in connections:
            connections[b] = set()
        connections[b].add(a)

    for pair in pairs:
        add_connection(pair[0], pair[1])

    computers = list(connections.keys())
    triplets = set()
    checked = set()
    for i in range(len(computers)):
        print(i)
        for j in range(len(computers)):
            for k in range(len(computers)):
                if i == j or j == k or i == k:
                    continue
                (a,b,c) = sorted([computers[i], computers[j], computers[k]])
                if (a, b, c) in checked:
                    continue
                checked.add((a, b, c))
                if b in connections[a] and c in connections[b] and a in connections[c]:
                    triplets.add((a, b, c))
    return list(triplets)

if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    kh-tc
    qp-kh
    de-cg
    ka-co
    yn-aq
    qp-ub
    cg-tb
    vc-aq
    tb-ka
    wh-tc
    yn-cg
    kh-ub
    ta-co
    de-co
    tc-td
    tb-wq
    wh-td
    ta-ka
    td-qp
    aq-cg
    wq-ub
    ub-vc
    de-ta
    wq-aq
    wq-vc
    wh-yn
    ka-de
    kh-ta
    co-tc
    wh-qp
    tb-vc
    td-yn
    """).strip()
    input = open("day23.txt").read()
    print(f"Part 1 test, 7 expected: {part1(test_input1)}")
    print(f"Part 1: {part1(input)}")

