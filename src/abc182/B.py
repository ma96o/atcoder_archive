N = int(input())
aList = list(map(int, input().split()))

ans = 0
beforeNums = 0
for i in range(2, max(aList) + 1):
    nums = len(list(filter(lambda v: v % i == 0, aList)))
    if beforeNums < nums:
        ans = i
        beforeNums = nums

print(ans)
