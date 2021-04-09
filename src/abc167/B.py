a, b, c, k = map(int, input().split())

if k <= a:
    print(k)
    exit()
elif k <= a+b:
    print(a)
else:
    print(a*2+b-k)
