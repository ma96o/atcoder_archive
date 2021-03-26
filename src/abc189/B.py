from decimal import Decimal

N, X = map(int, input().split())

sumAlc = 0
output = -1

for i in range(N):
    v, p = map(int, input().split())
    sumAlc = Decimal(f'{sumAlc}') + Decimal(f'{v * p / 100}')

    if Decimal(f'{X}') < Decimal(f'{sumAlc}'):
        output = i + 1
        break

print(output)
