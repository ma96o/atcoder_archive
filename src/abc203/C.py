# n, k = map(int, input().split())
# stock = k
# temp = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     if stock - (a - temp) < 0:
#         print(temp+stock)
#         exit()
#     stock = stock - (a-temp) + b
#     temp = a

# print(min(temp+stock, pow(10, 100)))


n, k = map(int, input().split())
stock = k
temp = 0
dict = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in dict.keys():
        dict[a] += b
    else:
        dict[a] = b

for k, v in sorted(dict.items(), key=lambda x: x[0]):
    if stock - (k - temp) < 0:
        print(temp+stock)
        exit()
    stock = stock - (k-temp) + v
    temp = k

print(min(temp+stock, pow(10, 100)))
