N, M, T = map(int, input().split())

output = 'Yes'

btr = N
preB = 0
for i in range(M):
    a, b = map(int, input().split())
    btr -= a-preB
    if btr <= 0:
        output = 'No'
        break

    btr += b - a
    if btr > N:
        btr = N
    preB = b

if btr-T+preB <= 0:
    output = 'No'


print(output)
