import re

f = open("input.txt", "r")
n = [int(s) for s in re.findall(r"(\d+)", f.read())]
A, B, C = n[0], n[1], n[2]
program = n[3:]
ip = 0
output = []

def combo(v):
    if v < 4:
        return v
    if v == 4:
        return A
    if v == 5:
        return B
    if v == 6:
        return C

def adv(v):
    global A
    A = A // 2 ** combo(v)
    return True

def bxl(v):
    global B
    B = B ^ v
    return True

def bst(v):
    global B
    B = combo(v) % 8
    return True

# The jnz instruction (opcode 3) does nothing if the A register is 0.
# However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
# if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
def jnz(v):
    global A, ip
    if A != 0:
        ip = v
        return False
    return True

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B.
# (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(v):
    global B, C
    B = B ^ C
    return True

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value.
# (If a program outputs multiple values, they are separated by commas.)
def out(v):
    output.append(combo(v) % 8)
    return True

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register.
# (The numerator is still read from the A register.)
def bdv(v):
    global A, B
    B = A // 2 ** combo(v)
    return True

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register.
# (The numerator is still read from the A register.)
def cdv(v):
    global A, C
    C = A // 2 ** combo(v)
    return True

ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while ip < len(program):
    op, v = program[ip], program[ip + 1]
    if ops[op](v):
        ip += 2

print(",".join(map(str, output)))
