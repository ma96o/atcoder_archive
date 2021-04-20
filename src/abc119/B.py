n = int(input())

ans = 0
for i in range(n):
    x, u = input().split()
    if u == "BTC":
        ans += 380000 * float(x)
    else:
        ans += int(x)

print(ans)
