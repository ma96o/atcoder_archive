n = int(input())

ans = 1
cnt = 0
for i in range(2, n+1)[::2]:
    target = i
    temp = 0
    while target % 2 == 0:
        temp += 1
        target = target // 2
    if temp > cnt:
        ans = i
        cnt = temp


print(ans)
