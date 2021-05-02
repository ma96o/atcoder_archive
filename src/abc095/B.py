n, x = map(int, input().split())
mlist = list(int(input()) for _ in range(n))
print((x - sum(mlist)) // min(mlist) + n)
