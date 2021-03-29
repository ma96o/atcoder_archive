A, B = input().split()

sumA = int(A[0]) + int(A[1]) + int(A[2])
sumB = int(B[0]) + int(B[1]) + int(B[2])

print(sumA if sumA > sumB else sumB)
