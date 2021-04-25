n, m, x, y = map(int, input().split())
maxX = max(max(map(int, input().split())), x)
minY = min(min(map(int, input().split())), y)

print("No War" if maxX < minY else "War")
