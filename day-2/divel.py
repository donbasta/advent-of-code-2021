#part 1
with open("input.in") as file:
    depth = 0
    loc = 0
    direction = {"up": -1, "down": 1}
    ar = list(map(lambda x: x.rstrip().split(), file.readlines()))
    for i in range(len(ar)):
        if ar[i][0] == "forward":
            loc += int(ar[i][1])
        else:
            depth += int(ar[i][1]) * direction[ar[i][0]]
    print(depth, loc, depth * loc)

#part 2
with open("input.in") as file:
    depth = 0
    loc = 0
    aim = 0
    direction = {"up": -1, "down": 1}
    ar = list(map(lambda x: x.rstrip().split(), file.readlines()))
    for i in range(len(ar)):
        if ar[i][0] == "forward":
            loc += int(ar[i][1])
            depth += aim * int(ar[i][1])
        else:
            aim += int(ar[i][1]) * direction[ar[i][0]]
    print(depth, loc, depth * loc)