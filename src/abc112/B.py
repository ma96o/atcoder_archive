n, T = map(int, input().split())
costs = []

for i in range(n):
    c, t = map(int, input().split())
    if t <= T:
        costs.append(c)

print(min(costs) if len(costs) != 0 else "TLE")
