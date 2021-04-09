n, m = map(int, input().split())
alist = list(map(int, input().split()))
ans = n - sum(alist)

print(ans if ans >= 0 else '-1')
