N, M = map(int, input().split())
aList = []
bList = []

for i in range(M):
    a, b = map(int, input().split())
    aList.append(a)
    bList.append(b)

K = int(input())
cList = []
dList = []

for i in range(K):
    c, d = map(int, input().split())
    cList.append(c)
    dList.append(d)


activePlate = []
activePlates = []
p = 0

for k in range(K):
    c = cList[k]
    d = dList[k]
    if d in activePlate:
        activePlate.append(c)
    elif c in activePlate:
        activePlate.append(d)
    else:
        activePlates[p] = activePlate.append(c)
        activePlates[p+1] = activePlate.append(d)
        p += 1
        # countC = cList[k:].count(c)
        # countD = dList[k:].count(d)
        # if countC > countD:
        #     activePlate.append(d)
        # else:
        #     activePlate.append(c)
        p

sumM = 0

for i in range(M):
    a = aList[i]
    b = bList[i]
    if a in activePlate and b in activePlate:
        sumM += 1

print(sumM)
