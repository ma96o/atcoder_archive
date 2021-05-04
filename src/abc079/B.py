n = int(input())

l_2 = 2
l_1 = 1

if n == 1:
    print(l_1)
    exit()

l = 0
for i in range(2, n+1):
    l = l_1 + l_2
    l_2 = l_1
    l_1 = l

print(l)
