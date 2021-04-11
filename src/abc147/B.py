s = input()
ls = len(s)

if ls % 2 == 0:
    bhs = s[:ls//2]
    ahs = s[ls//2:][::-1]
else:
    bhs = s[:(ls-1)//2]
    ahs = s[(ls+1)//2:][::-1]

cnt = 0
for i in range(len(bhs)):
    if bhs[i] != ahs[i]:
        cnt += 1

print(cnt)

# for i in range(ls // 2):
#     if s[i] != s[ls-1-i]:
#         cnt += 1

# print(sum(i != j for i, j in zip(s, s[::-1])) // 2)
