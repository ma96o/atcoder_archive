a, b = map(int, input().split())

print(str(a)*b if a <= b else str(b)*a)

# print(str(min(a, b) * max(a, b)))
