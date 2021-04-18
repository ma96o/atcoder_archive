r, d, x = map(int, input().split())

ans = []
for _ in range(10):
    nx = r*x - d
    ans.append(nx)
    x = nx

print(*ans, sep='\n')
