f = open("input.txt", "r")
codes = [list(l.strip()) for l in f.readlines()]


def find(keypad, key):
    for r, rr in enumerate(keypad):
        for c, cc in enumerate(rr):
            if cc == key:
                return (r, c)


dv = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
numpad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
dirpad = [["", "^", "A"], ["<", "v", ">"]]
pads = [numpad, dirpad, dirpad]

class keypad(object):

    def __init__(self, kp):
        self.kp = kp
        self.pos = find(kp, "A")

    def vh(self, new_pos):
        to_press = []
        if new_pos[0] > self.pos[0]:
            to_press += ["v"] * (new_pos[0] - self.pos[0])
        if new_pos[0] < self.pos[0]:
            to_press += ["^"] * (self.pos[0] - new_pos[0])

        if new_pos[1] > self.pos[1]:
            to_press += [">"] * (new_pos[1] - self.pos[1])
        if new_pos[1] < self.pos[1]:
            to_press += ["<"] * (self.pos[1] - new_pos[1])
        to_press += ["A"]
        return to_press

    def hv(self, new_pos):
        to_press = []
        if new_pos[1] > self.pos[1]:
            to_press += [">"] * (new_pos[1] - self.pos[1])
        if new_pos[1] < self.pos[1]:
            to_press += ["<"] * (self.pos[1] - new_pos[1])

        if new_pos[0] > self.pos[0]:
            to_press += ["v"] * (new_pos[0] - self.pos[0])
        if new_pos[0] < self.pos[0]:
            to_press += ["^"] * (self.pos[0] - new_pos[0])
        to_press += ["A"]
        return to_press

    def press(self, k):
        new_pos = self.pos
        new_pos = find(self.kp, k)
        res = []

        res = [p for p in [self.hv(new_pos), self.vh(new_pos)] if self.ok(p)]
        self.pos = new_pos
        return res

    def ok(self, path):
        pos = self.pos
        for p in path[:-1]:
            pos = (pos[0] + dv[p][0], pos[1] + dv[p][1])
            if self.kp[pos[0]][pos[1]] == "":
                return False
        return True

    def press_fwd(self, k):
        if k == "A":
            return self.kp[self.pos[0]][self.pos[1]]
        self.pos = (self.pos[0] + dv[k][0], self.pos[1] + dv[k][1])
        if self.kp[self.pos[0]][self.pos[1]] == "":
            raise ValueError("Invalid move")
        return ""


def permute(l):
    # generate all permutations of a list of lists
    if len(l) == 1:
        return [[ll] for ll in l[0]]
    else:
        return [[a] + b for a in l[0] for b in permute(l[1:])]


def filtermin(l):
    l = list(l)
    ml = minlen(l)
    return [x for x in {"".join(ll) for ll in l if len(ll) == ml}]


def minlen(l):
    return min([len(ll) for ll in l])


total = 0
for code in codes:
    to_type = [code]
    for p in pads:
        opts = []
        for tt in to_type:
            kp = keypad(p)
            presses = [[] for _ in range(len(tt))]
            for i, k in enumerate(tt):
                presses[i] += filtermin(kp.press(k))
            opts += permute(presses)

        to_type = filtermin(opts)
        # print(code, to_type)

    path = "".join(filtermin(to_type)[0])
    for pad in reversed(pads):
        kp = keypad(pad)
        path = "".join([kp.press_fwd(k) for k in path])
    print(
        code,
        minlen(to_type),
        int("".join(code[:3])),
        path,
        "".join(filtermin(to_type)[0]),
    )
    total += minlen(to_type) * int("".join(code[:3]))
print(total)
