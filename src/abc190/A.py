A, B, C = map(int, input().split())

a = "Aoki"
t = "Takahashi"
output = a

if A == B and C == 1:
    output = t
elif A > B:
    output = t

print(output)
