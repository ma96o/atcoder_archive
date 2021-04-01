N, X = map(int, input().split())
S = input()

point = X

for i in range(N):
    s = S[i]
    if s == 'x':
        point -= 1
    elif s == 'o':
        point += 1
    if point < 0:
        point = 0


print(point)
