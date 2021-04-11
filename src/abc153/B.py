h, n = map(int, input().split())
alist = list(map(int, input().split()))

print("Yes" if h <= sum(alist) else "No")
