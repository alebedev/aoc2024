import textwrap

def part1(input: str):
    compressed = compress(parse_input(input))
    return checksum(compressed)

def part2(input: str):
    compressed = defrag_compress(parse_input(input))
    return checksum(compressed)

def parse_input(input: str):
    result = []
    id = 0
    for (i,char) in enumerate(input):
        assert char.isdigit()
        size = int(char)
        for j in range(size):
            if i % 2 == 0:
                result.append(id)
            else:
                result.append(None)
        if i % 2 == 0:
            id += 1
    return result

def parse_chunks(input: str):
    result = []
    id = 0
    for (i,char) in enumerate(input):
        assert char.isdigit()
        size = int(char)
        if i % 2 == 0:
            result.append((id, size))
            id += 1
        else:
            result.append((None, size))
    return result

def compress(list):
    result = list.copy()
    i = 0
    j = len(list) - 1
    while i < j:
        if result[i] is not None:
            i += 1
        elif result[j] is not None:
            result[i] = result[j]
            result[j] = None
            j -= 1
        else:
            j -= 1
    return result

def checksum(list):
    sum = 0
    for (i,x) in enumerate(list):
        if x != None:
            sum += i * x
    return sum

def defrag_compress(list):
    result = list.copy()
    i = 0
    j = len(list) - 1
    while i < j:
        if result[i] is not None:
            i += 1
        elif result[j] is not None:
            cur_id = result[j]
            while j > 0:
                if result[j - 1] == cur_id:
                    j -= 1
                else:
                    break
            cur_size = chunk_size(result, j)

            k = i
            while k < j:
                if result[k] is None:
                    empty_size = chunk_size(result, k)
                    if empty_size >= cur_size:
                        break
                    else:
                        if k + empty_size < j:
                            k += empty_size
                        else: break
                else:
                    k += 1
            # print(f"Chunk {cur_id} at {j}, size {cur_size}, first empty: {k}, empty size: {chunk_size(result, k)}")
            if k < j and chunk_size(result, k) >= cur_size:
                for x in range(cur_size):
                    result[k + x] = cur_id
                    result[j + x] = None
            # print(result, i, j)
            j -= 1
        else:
            j -= 1

    return result

def chunk_size(list, i):
    id = list[i]
    size = 1
    for j in range(i + 1, len(list)):
        if list[j] == id:
            size += 1
        else:
            break
    return size

if __name__ == "__main__":
    test_input = "2333133121414131402"
    input = open('day9.txt').read()
    print(f"Part 1 test, 1928 expected: {part1(test_input)}")
    print(f"Part 1: {part1(input)}")

    print(f"Part 2 test, 2858 expected: {part2(test_input)}")
    print(f"Part 2: {part2(input)}")