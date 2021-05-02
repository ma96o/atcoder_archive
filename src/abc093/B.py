a, b, k = map(int, input().split())
r = list(range(a, b+1))  # なぜかここで RE になる
ns = list(set(r[:k] + r[::-1][:k]))
print(*sorted(ns), sep='\n')
