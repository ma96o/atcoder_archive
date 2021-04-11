n = int(input())

if n > 81:
    print("No")
    exit()

for i in range(1, 10):
    if n % i == 0:
        for j in range(i, 10):
            if i * j == n:
                print("Yes")
                exit()

print("No")
