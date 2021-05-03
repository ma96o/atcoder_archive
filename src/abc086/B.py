a, b = input().split()
print("Yes" if float(pow(int(a+b), 0.5)).is_integer() else "No")
