n, k = map(int, input().split())

havings = set()

for i in range(k):
    d = input()
    aset = set(list(map(int, input().split())))
    havings |= aset

ans = 0
for i in range(1, n+1):
    if not i in havings:
        ans += 1


print(ans)
