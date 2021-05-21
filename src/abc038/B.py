h1, w1 = map(int, input().split())
d2 = list(map(int, input().split()))
print("YES" if h1 in d2 or w1 in d2 else "NO")
