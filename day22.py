import textwrap

def part1(input: str):
    last_prices = [prices(num, 2000)[-1] for num in parse_input(input)]
    return sum(last_prices)

def part2(input: str):
    pass

def parse_input(input: str):
    return [
        int(line) for line in input.splitlines()
    ]

def prices(seed, count):
    prices = [seed]
    for x in range(count):
        prices.append(derive(prices[-1]))
    return prices[1:]

def derive(seed):
    result = prune(mix(seed, seed * 64))
    result = prune(mix(result, result // 32))
    result = prune(mix(result, result * 2048))
    return result

def mix(a, b):
    return a ^ b

def prune(val):
    return val % 16777216

if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    1
    10
    100
    2024
    """).strip()
    input = open("day22.txt").read()
    print(f"Prices from 123: {prices(123, 10):}")
    print(f"Part 1 test, 37327623 expected: {part1(test_input1)}")
    print(f"Part 1: {part1(input)}")
