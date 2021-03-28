N = int(input())
aList = list(map(int, input().split()))

halfNum = 2**(N-1)
firstHalf = aList[:halfNum]
secondHalf = aList[halfNum:]

maxFirstHalf = max(firstHalf)
maxSecondHalf = max(secondHalf)

index = 0
if maxFirstHalf > maxSecondHalf:
    index = aList.index(maxSecondHalf) + 1
else:
    index = aList.index(maxFirstHalf) + 1

print(index)
