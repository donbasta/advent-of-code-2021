with open("input.in") as file:
    ar = list(map(lambda x: x.rstrip(), file.readlines()))
    sz = len(ar[0])
    cnt = [0 for _ in range(sz)]
    for i in range(len(ar)):
        for j in range(sz):
            if ar[i][j] == '1':
                cnt[j] += 1
    mask = 2 ** sz - 1
    gamma = 0
    for i in range(sz):
        if cnt[i] * 2 >= len(ar):
            gamma += 2 ** (sz - i - 1)
    epsilon = mask - gamma
    print(gamma, epsilon, gamma * epsilon)

with open("input.in") as file:
    ar = list(map(lambda x: x.rstrip(), file.readlines()))
    sz = len(ar[0])
    mp = {}
    for i in range(len(ar)):
        tmp = 0
        for j in range(sz):
            tmp *= 2
            if ar[i][j] == '1':
                tmp += 1
            if (tmp,j) not in mp:
                mp[(tmp,j)] = 0
            mp[(tmp,j)] += 1

    x, y = 0, 0
    dx, dy = False, False
    for i in range(sz):
        for u in [x*2, x*2+1, y*2, y*2+1]:
            if (u,i) not in mp:
                mp[(u,i)] = 0

        if mp[(x * 2, i)] == 0:
            x = x * 2 + 1
        elif mp[(x * 2 + 1, i)] == 0:
            x = x * 2
        elif mp[(x * 2,i)] > mp[(x * 2 + 1,i)]:
            x = x * 2
        else:
            x = x * 2 + 1
        
        if mp[(y * 2, i)] == 0:
            y = y * 2 + 1
        elif mp[(y * 2 + 1, i)] == 0:
            y = y * 2
        elif mp[(y * 2,i)] > mp[(y * 2 + 1,i)]:
            y = y * 2 + 1
        else:
            y = y * 2

    print(x, y, x*y)
