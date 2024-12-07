total = 0
op = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]


def inc(v):
    "ternary increment"
    um = 1
    for i in range(len(v)):
        n = v[i] + um
        um = 0
        if n == 3:
            v[i] = 0
            um = 1
        else:
            v[i] = n
            return v
    return v


def calc(X, v):
    y = X[0]
    for j in range(1, len(X)):
        y = op[v[j - 1]](y, X[j])

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

    v = [0] * (len(X) - 1)
    for i in range(3 ** (len(X) - 1)):
        if calc(X, v) == y:
            total += y
            break
        v = inc(v)

print(total)
