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


# for a in range(7):
#     if 2**a <= n and n < 2**(a+1):
#         print(str(2**a))

# ans = 1
# while ans <= n/2:
#     ans *= 2
# print(ans)

# n = bin(int(input()))
# print(1 << len(n[2:])-1)
