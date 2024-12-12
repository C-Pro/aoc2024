


f = open("input.txt", "r", encoding="utf-8")
stones = f.read().strip().split(" ")

def blink(ss):
    sss = []
    for s in ss:
        if s == "0":
            sss.append("1")
            continue
        if len(s) % 2 == 0:
            sss.append(s[:len(s)//2])
            sss.append(str(int(s[len(s)//2:])))
            continue
        sss.append(str(int(s)*2024))

    return sss

total = 0
for s in stones:
    ss = [s]
    for i in range(25):
        ss = blink(ss)
    total += len(ss)

print(total)
