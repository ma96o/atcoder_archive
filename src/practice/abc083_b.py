N, A, B = map(int, input().split())

output = 0
for target in range(N + 1):
    targetSum = 0
    for n in [int(i) for i in str(target)]:
        targetSum += int(n)
    if targetSum > B:
        continue
    if targetSum >= A:
        output += target


print(output)
