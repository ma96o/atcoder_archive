w, a, b = map(int, input().split())
if a+w <= b:
    print(b - a-w)
else:
    print(max(0, a-b-w))
