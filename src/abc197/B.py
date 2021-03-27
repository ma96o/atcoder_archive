H, W, X, Y = map(int, input().split())

sList = [input() for i in range(H)]

count = 0

if sList[X-1][Y-1] == '.':
    count += 1

for i in range(1, W):
    if Y - 1 - i < 0 or sList[X-1][Y-1-i] == '#':
        break
    count += 1

for i in range(1, W):
    if Y - 1 + i >= W or sList[X-1][Y-1+i] == '#':
        break
    count += 1

for i in range(1, H):
    if X - 1 - i < 0 or sList[X-1-i][Y-1] == '#':
        break
    count += 1

for i in range(1, H):
    if X - 1 + i >= H or sList[X-1+i][Y-1] == '#':
        break
    count += 1

print(count)
