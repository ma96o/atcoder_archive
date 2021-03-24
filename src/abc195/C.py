N = int(input())

singleSum = 10 ** 6 - \
    10 ** 3 if N >= 10 ** 6 else (N - 10 ** 3 + 1) if N >= 10 ** 3 else 0
doubleSum = 10 ** 9 - \
    10 ** 6 if N >= 10 ** 9 else (N - 10 ** 6 + 1) if N >= 10 ** 6 else 0
tripleSum = 10 ** 12 - \
    10 ** 9 if N >= 10 ** 12 else (N - 10 ** 9 + 1) if N >= 10 ** 9 else 0
quadrupleSum = 10 ** 15 - \
    10 ** 12 if N >= 10 ** 15 else (N - 10 ** 12 + 1) if N >= 10 ** 12 else 0
quintupleSum = 1 if N == 10 ** 15 else 0

print(1 * singleSum + 2 * doubleSum + 3 *
      tripleSum + 4 * quadrupleSum + 5 * quintupleSum)
