import multiprocessing
from functools import cache

f = open("input.txt", "r", encoding="utf-8")
stones = [int(c) for c in f.read().strip().split(" ")]


@cache
def count(n, t):
    if t == 0:
        return 1

    if n == 0:
        return count(1, t-1)

    s = str(n)
    if len(s) % 2 == 0:
        return  count(int(s[:len(s)//2]), t-1) + count(int(s[len(s)//2:]), t-1)

    return count(n*2024, t-1)

def f(x):
    return count(x, 75)

if __name__ == "__main__":

    with multiprocessing.Pool() as pool:
        results = pool.map(f, stones)
        total = sum(results)

    print(total)
