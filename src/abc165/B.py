x = int(input())

c = 100
i = 1
while True:
    c += c // 100
    if c >= x:
        print(i)
        exit()
    i += 1
