A, B = map(int, input().split())
X = A + B
output = 4

if 15 <= X and 8 <= B:
    output = 1
elif 10 <= X and 3 <= B:
    output = 2
elif 3 <= X:
    output = 3

print(output)
