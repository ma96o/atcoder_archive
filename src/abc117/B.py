n = int(input())
l = list(map(int, input().split()))

maxl = max(l)
print("Yes" if maxl*2 < sum(l) else "No")
