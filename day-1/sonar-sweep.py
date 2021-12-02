#day 1 part 1
with open("input.in") as file:
    ans = 0
    ar = list(map(lambda x: int(x.rstrip()), file.readlines()))
    for i in range(1,len(ar)):
        if ar[i] > ar[i - 1]:
            ans += 1
    print(ans)

#day 1 part 2
with open("input.in") as file:
    ans = 0
    ar = list(map(lambda x: int(x.rstrip()), file.readlines()))
    for i in range(3,len(ar)):
       if  ar[i] > ar[i - 3]:
            ans += 1
    print(ans)
