N = int(input())

count = 0
for item in range(1, N+1):
    if '7' in str(item) or '7' in oct(item):
        count += 1

print(N - count)
