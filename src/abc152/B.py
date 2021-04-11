a, b = map(int, input().split())

print(str(a)*b if a <= b else str(b)*a)

# print(str(min(a, b) * max(a, b)))

sa = str(a)*b
sb = str(b)*a
print([sb, sa][a < b])
