d, n = input().split()
n = '101' if n == '100' else n
print(n + str(100**int(d))[1:])
