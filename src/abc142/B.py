n, k = map(int, input().split())
hlist = list(map(int, input().split()))
print(len(list(filter(lambda h: h >= k, hlist))))

# print(len([i for i in range(n) if hlist[i] >= k]))
