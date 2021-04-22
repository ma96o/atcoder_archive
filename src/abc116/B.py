s = int(input())

a = s
alist = [a]
for i in range(2, 100000):
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3*a + 1
    if a in alist:
        print(i)
        exit()
    alist.append(a)
