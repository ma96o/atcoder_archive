n = int(input())
left7 = n % 7
left4 = n % 4

if n % 7 == 0 or n % 4 == 0 or left7 % 4 == 0 or left4 % 7 == 0:
    print("Yes")
    exit()

print("No")
