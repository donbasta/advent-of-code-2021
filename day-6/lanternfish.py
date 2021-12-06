with open("input.in") as file:
    a = list(map(int, file.readline().split(",")))
    cnt = [0 for _ in range(10)]
    for t in a:
        assert t < 10
        cnt[t] += 1
    for _ in range(256):
        tmp = [0 for _ in range(10)]
        for i in range(8):
            tmp[i] = cnt[i + 1]
        tmp[8] = cnt[0]
        tmp[6] += cnt[0]
        cnt = tmp
    print(sum(cnt))
