n, k, m = map(int, input().split())
alist = list(map(int, input().split()))

x = n*m - sum(alist)
x = x if x >= 0 else 0

print(x if x <= k else -1)


# print(-1 if x > k else max(0, x))
