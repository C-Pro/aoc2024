import re

f = open("input.txt", "r")
n = [int(s) for s in re.findall(r"(\d+)", f.read())]
A, B, C = n[0], n[1], n[2]
program = n[3:]
ip = 0


class Comp(object):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.ip = 0

    def combo(self,v):
        if v < 4:
            return v
        if v == 4:
            return self.A
        if v == 5:
            return self.B
        if v == 6:
            return self.C

    def adv(self, v):
        self.A = self.A // 2 ** self.combo(v)
        return True

    def bxl(self, v):
        self.B = self.B ^ v
        return True

    def bst(self, v):
        self.B = self.combo(v) % 8
        return True

    def jnz(self,v):
        if self.A != 0:
            self.ip = v
            return False
        return True

    def bxc(self, v):
        self.B = self.B ^ self.C
        return True

    def out(self, v):
        return self.combo(v) % 8

    def bdv(self,v):
        self.B = self.A // 2 ** self.combo(v)
        return True

    def cdv(self,v):
        self.C = self.A // 2 ** self.combo(v)
        return True

    def call(self, opc, v):
        if opc == 5:
            self.ip += 2
            return self.out(v)

        ops = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
        if ops[opc](v):
            self.ip += 2
        return None




A = 1
while True:
    c = Comp(A, B, C)
    i = 0
    while c.ip < len(program):
        v = c.call(program[c.ip], program[c.ip + 1])
        if v is not None:
            if v == program[i]:
                print(v, end=",")
                i += 1
                if i == len(program):
                    print(A)
                    exit()
            else:
                if i>0:
                    print(A)
                break
    A += 1
