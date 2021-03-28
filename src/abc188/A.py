X, Y = map(int, input().split())

output = 'No'
if (X > Y and X < Y + 3) or (X < Y and X + 3 > Y):
    output = 'Yes'

print(output)
