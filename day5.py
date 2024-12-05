import textwrap

def part1(input: str) -> int:
    adj_list, requests = input.split("\n\n")
    graph = parse_graph(adj_list)
    # print("deps: %s" % graph)
    sum = 0
    for line in requests.splitlines():
        req = [int(x) for x in line.split(",")]
        if (is_valid_order(req, graph)):
            # print("valid %s" % req)
            sum += req[len(req) // 2]
    return sum

def parse_graph(adj_list: str) -> dict[int, set[int]]:
    result = {}
    for line in adj_list.splitlines():
        a, b = map(int, line.split("|"))
        if a not in result:
            result[a] = set()
        result[a].add(b)
    return result

def is_valid_order(order: list[str], graph: dict[set[int]]) -> bool:
    for (i,item) in enumerate(order):
        rest = order[i+1:]
        for x in rest:
            if x not in graph:
                continue
            if item in graph[x]:
                return False
    return True

def part2(input: str) -> int:
    adj_list, requests = input.split("\n\n")
    graph = parse_graph(adj_list)
    # print("deps: %s" % graph)
    print("top_order: %s" % top_order(graph) )
    sum = 0
    master_order = {item: i for (i, item) in enumerate(top_order(graph))}
    print("master_order: %s" % master_order)
    for line in requests.splitlines():
        req = [int(x) for x in line.split(",")]
        if not is_valid_order(req, graph):
            valid_order = sorted(req, key = lambda x: master_order[x] if x in master_order else -1)
            print("invalid %s" % req)
            print("valid: %s" % valid_order)
            sum += valid_order[len(req) // 2]
    return sum

def top_order(graph: dict[int, set[int]]) -> list[int]:
    result = []
    visited = set()
    def visit(x: int):
        if x in visited:
            return
        visited.add(x)
        if x in graph:
            for n in graph[x]:
                visit(n)
        result.insert(0, x)
    for key in graph.keys():
        visit(key)
    return result


if __name__ == "__main__":
    test_input = textwrap.dedent("""
    47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
    
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47
    """).strip()
    input = open("day5.txt").read()

    print("Part 1 test, 143 expected: %s" % part1(test_input))
    print("Part 1: %s" % part1(input))

    print("Part 2 test, 123 expected: %s" % part2(test_input))
    print("Part 2: %s" % part2(input))