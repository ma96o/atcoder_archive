n = int(input())
pwr = 1
for i in range(1, n+1):
    pwr *= i

print(pwr % (10**9 + 7))
