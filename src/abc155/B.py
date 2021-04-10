n = int(input())
alist = filter(lambda n: n % 2 == 0, map(int, input().split()))

for a in alist:
    if a % 3 != 0 and a % 5 != 0:
        print("DENIED")
        exit()

print("APPROVED")
