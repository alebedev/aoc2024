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
    pairs = parse_input(input)
    groups = find_groups(pairs)
    largest_group = max(groups, key=len)
    return ','.join(sorted(largest_group))

def parse_input(input: str):
    pairs = [
        (line.split("-")[0], line.split("-")[1])
        for line in input.splitlines()
    ]
    return pairs

def find_triplets(pairs):
    connections = find_connections(pairs)
    computers = list(connections.keys())
    triplets = set()
    checked = set()
    for i in range(len(computers)):
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

def find_connections(pairs):
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

    return connections

def find_groups(pairs):
    connections = find_connections(pairs)
    computers = set()
    for (a,b) in pairs:
        computers.add(a)
        computers.add(b)
    groups = [{c} for c in computers]
    while True:
        has_joined = False
        for group_a in groups:
            for computer in computers:
                if computer in group_a:
                    continue
                if all_connected(group_a, {computer}, connections):
                    groups.remove(group_a)
                    groups.append(group_a.union({computer}))
                    # print('joined', group_a, computer)
                    has_joined = True
                    break
        if not has_joined:
            break

    return list(groups)

def all_connected(group_a, group_b, connections):
    for a in group_a:
        for b in group_b:
            if b not in connections[a]:
                return False
    return True

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
    # print(f"Part 1: {part1(input)}")

    print(f"Part 2 test, 'co,de,ka,ta' expected: {part2(test_input1)}")
    print(f"Part 2: {part2(input)}")
