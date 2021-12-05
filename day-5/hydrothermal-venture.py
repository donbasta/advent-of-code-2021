with open("input.in") as file:
    lines = file.readlines()
    cnt = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        t = list(map(lambda x: x.strip(), line.split("->")))
        a = list(map(int, t[0].split(",")))
        b = list(map(int, t[1].split(",")))
        if a[0] == b[0]:
            for i in range(min(a[1], b[1]), max(a[1], b[1]) + 1):
                cnt[a[0]][i] += 1
        elif a[1] == b[1]:
            for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                cnt[i][a[1]] += 1
        else:
            assert (a[0] + a[1] == b[0] + b[1]) or (a[0] - a[1] == b[0] - b[1])
            if a[0] + a[1] == b[0] + b[1]:
                for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    cnt[i][a[0] + a[1] - i] += 1
            elif a[0] - a[1] == b[0] - b[1]:
                for i in range(min(a[0], b[0]), max(a[0], b[0]) + 1):
                    cnt[i][i + a[1] - a[0]] += 1
    ans = 0
    for i in range(1000):
        for j in range(1000):
            if cnt[i][j] > 1:
                ans += 1
    print(ans)
