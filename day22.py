import sys
import textwrap

def part1(input: str):
    last_prices = [gen_secrets(num, 2000)[-1] for num in parse_input(input)]
    return sum(last_prices)

def part2(input: str):
    seeds = parse_input(input)
    secrets = {
        seed: gen_secrets(seed, 2000)
        for seed in seeds
    }
    all_seqs = {}
    for (seed, secrets) in secrets.items():
        prices = [x % 10 for x in secrets]
        diffs = [x - y for x, y in zip(prices[1:], prices)]
        for (price, diff0, diff1, diff2, diff3) in zip(prices[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
            seq = (diff0, diff1, diff2, diff3)
            if seq not in all_seqs:
                all_seqs[seq] = {}
            if seed not in all_seqs[seq]:
                all_seqs[seq][seed] = price
    print(f"Possible sequences: {len(all_seqs)}")
    result = 0
    for (seq, prices) in all_seqs.items():
        cur = sum(prices.values())
        result = max(result, cur)
    # print(f"Result: {result}")
    return result
    # best_seq = max(all_seqs, key=lambda seq: sum_at_seq(seeds, seq))
    # return sum_at_seq(seeds, best_seq)

def parse_input(input: str):
    return [
        int(line) for line in input.splitlines()
    ]

def gen_secrets(seed, count):
    prices = [seed]
    for x in range(count):
        prices.append(derive(prices[-1]))
    return prices

def derive(seed):
    result = prune(mix(seed, seed * 64))
    result = prune(mix(result, result // 32))
    result = prune(mix(result, result * 2048))
    return result

def mix(a, b):
    return a ^ b

def prune(val):
    return val % 16777216

def first_price_at_seq(secrets, seq):
    prices = [x % 10 for x in secrets]
    diffs = [x - y for x, y in zip(prices[1:], prices)]

    for (price, diff0, diff1, diff2, diff3) in zip(prices[4:], diffs,diffs[1:],diffs[2:],diffs[3:]):
        seq_at_price = (diff0, diff1, diff2, diff3)
        # print(f"{price}: {seq_at_price}")
        if seq_at_price == seq:
            return price
    return 0

secrets_cache = {}
def sum_at_seq(seeds, seq):
    sum = 0
    for x in seeds:
        secrets = secrets_cache.get(x)
        if not secrets:
            secrets = gen_secrets(x, 2000)
            secrets_cache[x] = secrets
        price = first_price_at_seq(secrets, seq)
        # print(f"{x}: {price}")
        sum += price
    sys.stdout.write(".")
    return sum


if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    1
    10
    100
    2024
    """).strip()
    input = open("day22.txt").read()
    print(f"Prices from 123: {gen_secrets(123, 11):}")
    print(f"Part 1 test, 37327623 expected: {part1(test_input1)}")
    # print(f"Part 1: {part1(input)}")

    test_input2 = textwrap.dedent("""
    1
    2
    3
    2024
    """).strip()
    print(f"Prices from 123: {[x % 10 for x in gen_secrets(123, 10)]}")
    print(f"Part 2 test, 23 expected: {sum_at_seq(parse_input(test_input2),  (-2,1,-1,3))}")
    # print(f"Part 2 test 2, 23 expected: {part2(test_input2)}")
    print(f"Part 2: {part2(input)}")