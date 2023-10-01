from functools import cache


@cache
def distance() -> None:
    r = []

    k = 3
    a = [3, 2, 5, 1, 2]

    for i, v in enumerate(a):
        t = []
        for j in range(len(a)):
            if j != i:
                t.append(abs(v - a[j]))
        t = sorted(t)
        r.append(sum(t[:k]))

    print(" ".join(str(n) for n in r))


distance()

# k = int(input().split()[1])
# a = list(map(int, input().split()))
