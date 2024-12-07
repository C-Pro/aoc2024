total = 0
op = [lambda x, y: x + y, lambda x, y: x * y]


def calc(X, i):
    y = X[0]
    for j in range(1, len(X)):
        o = (i & (1 << (j - 1))) >> (j - 1)
        y = op[o](y, X[j])

    return y


f = open("input.txt", "r", encoding="utf-8")

for l in f.readlines():
    y, X = (s.strip() for s in l.split(":"))
    X = list(map(int, X.split()))
    y = int(y)

    if len(X) == 1 and y == X[0]:
        total += X[0]
        continue

    if len(X) == 0:
        continue

    v = 0
    for i in range(2 ** (len(X) - 1)):
        if calc(X, i) == y:
            total += y
            break

print(total)
