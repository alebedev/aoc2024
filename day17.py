import textwrap
import re

def part1(input: str):
    computer = parse_input(input)
    print(computer)
    out = computer.run()
    return out

def part2(input: str):
    return 0

class Computer(object):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.ip = 0
        self.program = []

    def __repr__(self):
        return f"A: {self.a}, B: {self.b}, C: {self.c}, program: {self.program}"

    def run(self):
        output = []
        while self.ip < len(self.program):
            op = self.program[self.ip]
            val = self.program[self.ip + 1]
            self.ip += 2
            match op:
                case 'adv': self.adv(val)
                case 'bdv': self.bdv(val)
                case 'cdv': self.cdv(val)

                case 'bxl': self.bxl(val)
                case 'bst': self.bst(val)
                case 'bxc': self.bxc()
                case 'jnz': self.jnz(val)
                case 'out': output.append(self.out(val))
                case _: raise Exception(f"Unknown op {op}")
        return ','.join(output)

    def adv(self, operand):
        self.a = self._dv(operand)

    def bdv(self, operand):
        self.b = self._dv(operand)

    def cdv(self, operand):
        self.c = self._dv(operand)

    def _dv(self, operand):
        num = self.a
        combo = self.combo_value(operand)
        res = num // (2 ** combo)
        # print('_dv', num, operand, bits, res)
        return res

    def bxl(self, val):
        res = self.b ^ val
        # print('bxl', val, res)
        self.b = res

    def bst(self, val):
        combo = self.combo_value(val)
        res = combo % 8
        # print('bst', combo, res)
        self.b = res

    def jnz(self, val):
        if self.a != 0:
            self.ip = val

    def bxc(self):
        res = self.b ^ self.c
        # print('bxc', res)
        self.b = res

    def out(self, val):
        value = self.combo_value(val)
        res = value % 8
        # print('out', val, res)
        return str(res)

    def combo_value(self, operand):
        match operand:
            case 0 | 1 | 2 | 3: return operand
            case 4: return self.a
            case 5: return self.b
            case 6: return self.c
            case _: raise Exception(f"Invalid combo operand {operand}")

def parse_input(input: str):
    (registers_str, instructions_str) = input.split("\n\n")
    computer = Computer()
    for line in registers_str.splitlines():
        m = re.match(r"Register ([A-C]): (\d+)", line)
        match m.group(1):
            case 'A':
                computer.a = int(m.group(2))
            case 'B':
                computer.b = int(m.group(2))
            case 'C':
                computer.c = int(m.group(2))
    instructions = []
    for opcode_str in instructions_str.replace("Program: ", "").split(","):
        instructions.append(int(opcode_str))
    for x in range(0, len(instructions), 2):
        opcode = instructions[x]
        operand = instructions[x + 1]
        computer.program.append(OPCODES[opcode])
        computer.program.append(operand)
    return computer

OPCODES = {
    0: 'adv',
    1: 'bxl',
    2: 'bst',
    3: 'jnz',
    4: 'bxc',
    5: 'out',
    6: 'bdv',
    7: 'cdv'
}

if __name__ == "__main__":
    test_input1 = textwrap.dedent("""
    Register A: 729
    Register B: 0
    Register C: 0
    
    Program: 0,1,5,4,3,0
    """).strip()
    input = open("day17.txt").read()
    print(f"Part 1 test, '4,6,3,5,6,3,5,2,1,0' expected: {part1(test_input1)}")
    print(f"Part 1: {part1(input)}")

    # print(f"Part 2 test, 45 expected: {part2(test_input1)}")
    # print(f"Part 2: {part2(input)}")
