N = int(input())

count = 0
a = 1
while a*a < N:
    b = a
    while a*b < N:
        if a == b:
            count += 1
        else:
            count += 2
        b += 1
    a += 1

print(count)
