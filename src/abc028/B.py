s = input()
ans = []
for a in ['A', 'B', 'C', 'D', 'E', 'F']:
    ans.append(s.count(a))

print(*ans, sep=' ')
