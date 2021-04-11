n = int(input())
cnt = 0

if n < 2:
    print(0)
    exit()

cnt = 1
for a in range(1, n-2):
    b = n-a
    if b >= 1:
        cnt += 1

print(cnt)
