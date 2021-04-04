N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    # ans += sum(list(range(a, b+1)))
    ans += (b * (b+1) - a * (a+1)) // 2 + a


print(ans)
