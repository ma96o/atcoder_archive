N = input()
nums = list(map(int, input().split()))
nums.sort(reverse=True)
isAlice = 1
aliceScore = 0
bobScore = 0

for n in nums:
    if isAlice:
        aliceScore += n
        isAlice = 0
    else:
        bobScore += n
        isAlice = 1

print(aliceScore - bobScore)
