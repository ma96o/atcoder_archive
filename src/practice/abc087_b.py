A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(A + 1):
    if X - 500 * a < 0:
        continue
    for b in range(B + 1):
        if X - 500 * a - 100 * b < 0:
            continue
        for c in range(C + 1):
            if X - 500 * a - 100 * b - 50 * c == 0:
                count += 1

print(count)
