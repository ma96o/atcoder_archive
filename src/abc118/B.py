n, m = map(int, input().split())
targets = set(range(1, m+1))

for i in range(n):
    inputs = list(map(int, input().split()))
    targets = set(inputs[1:]) & targets

print(len(targets))

# targets = list(range(1, m+1))

# for i in range(n):
#     inputs = list(map(int, input().split()))
#     k = inputs[0]
#     alist = inputs[1:]
#     print('targets', targets)
#     for t in targets:
#         print('t', t, not t in alist)
#         if not t in alist:
#             targets.remove(t)

# print(len(targets))
