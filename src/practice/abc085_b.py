N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort(reverse=True)

count = 0
preNum = 101
for n in nums:
    if n < preNum:
        count += 1
    preNum = n

print(count)
