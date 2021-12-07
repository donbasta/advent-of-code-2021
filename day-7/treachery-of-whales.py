with open("input.in") as file:
    a = file.readline()
    pos = list(map(int, a.split(",")))
    l = min(pos)
    r = max(pos)

    def f(x):
        return sum(list(map(lambda k: abs(k - x) * (abs(k - x) + 1) // 2, pos)))

    ans = 2000000000
    for i in range(l, r + 1):
        ans = min(ans, f(i))
    print(ans)
