N = int(input())
aList = []
bList = []

for i in range(N):
    a, b = map(int, input().split())
    aList.append(a)
    bList.append(b)

minA = min(aList)
minB = min(bList)
genius = []
output = max(minA, minB)

for i, a in enumerate(aList):
    b = bList[i]
    if a == minA and b == minB:
        genius.append(i)

if len(genius) == 1:
    nextMinA = sorted(aList)[1]
    nextMinB = sorted(bList)[1]
    output = min(minA + minB, min(max(minA, nextMinB), max(nextMinA, minB)))

print(output)

# ↓ proto
# minA = min(aList)
# minB = min(bList)
# output = ""

# minableA = 10 ** 5
# minableB = 10 ** 5
# minSum = 0

# for i, a in enumerate(aList):
#     b = bList[i]
#     if a == minA and b == minB:
#         minSum = a + b
#     else:
#         minableA = min(a, minableA) if not a == minA else minableA
#         minableB = min(b, minableB) if not b == minB else minableB

# if minSum == 0:
#     output = max(minA, minB)
# elif minSum < minableA and minSum < minableB:
#     output = minSum
# else:
#     output = min(minSum, min(max(minableA, minB), max(minA, minableB)))

# print(output)


# minIndexesA = [i for i, v in enumerate(aList) if v == min(aList)]
# minIndexesB = [v for i, v in enumerate(bList) if v == min(bList) and minIdexes]
# doubleMinIndexes = list(set(minIndexesA) & set(minIndexesB))
