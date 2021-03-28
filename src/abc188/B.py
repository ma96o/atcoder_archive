N = int(input())
aList, bList = [list(map(int, input().split())) for i in range(2)]

sum = 0
for i, a in enumerate(aList):
    b = bList[i]
    sum += a * b

output = "Yes" if sum == 0 else "No"
print(output)
