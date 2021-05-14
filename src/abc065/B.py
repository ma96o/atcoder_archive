n = int(input())
alist = list(int(input()) for _ in range(n))

a = 1
pushed = []
cnt = 0
while a not in pushed:
    pushed.append(a)
    a = alist[a-1]
    cnt += 1
    if a == 2:
        print(cnt)
        exit()

print(-1)
