x, y = map(int, input().split())

j1 = y // 2 - x
j2 = x*2 - y // 2

if y % 2 == 0 and j1 >= 0 and j1 <= 25 and j2 >= 0 and j2 <= 50:
    print('Yes')
    exit()

print('No')

# if y % 2 == 0 and y >= 2*x and y <= 4*x:
#     print("Yes")
