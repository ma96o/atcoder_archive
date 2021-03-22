N = int(input())
nums = list(map(int, input().split()))
count = 0
newNums = nums

while True:
    newNums = list(map(lambda n: n // 2 if n % 2 == 0 else 0, newNums))
    count += 1
    if newNums.count(0) != 0:
        break

print(count - 1)
