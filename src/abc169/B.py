n = int(input())
alist = list(map(int, input().split()))

if 0 in alist:
    print(0)
    exit()

ans = 1

for i in range(n):
    ans *= alist[i]
    if ans > 10**18:
        ans = -1
        break

print(ans)
