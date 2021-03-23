N, Y = map(int, input().split())

A = -1
B = -1
C = -1

y = Y // 1000

# y = 10 * a + 5 * b + c

if y == N:
    A = 0
    B = 0
    C = N
elif y == 10 * N:
    A = N
    B = 0
    C = 0
elif N < y and y < 10 * N:
    for a in range(N)[::-1]:
        if y <= 10 * a and y - (10 * a) > 5 * (N - a):
            continue
        for b in range(N - a + 1)[::-1]:
            if y - (10 * a) < 5 * b and y - (10 * a) - (5 * b) > (N - a - b):
                continue
            for c in range(N - a - b + 1)[::-1]:
                if y - (10 * a) - (5 * b) != c or a + b + c != N:
                    continue
                A = a
                B = b
                C = c
                break
            else:
                continue
            break
        else:
            continue
        break

print(A, B, C)
