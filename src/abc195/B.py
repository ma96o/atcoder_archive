import math
A, B, W = map(int, input().split())

W = W * 1000

# W / B <= N and N <= W / A
minN = math.ceil(W / B)
maxN = math.floor(W / A)

if minN <= maxN:
    print(minN, maxN)
else:
    print("UNSATISFIABLE")
