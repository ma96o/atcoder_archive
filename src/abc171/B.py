n, k = map(int, input().split())
pList = [map(int, input().split())]
pList.sort()

print(sum(pList[:k]))
