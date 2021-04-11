n, k, m = map(int, input().split())
alist = list(map(int, input().split()))

x = n*m - sum(alist)
x = x if x >= 0 else 0

print(x if x <= k else -1)
