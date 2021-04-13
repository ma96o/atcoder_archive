S = input()

for i in range(1, len(S)+1):
    s = S[i-1]
    if i % 2 == 0:
        if not s in ['L', 'U', 'D']:
            print("No")
            exit()
    else:
        if not s in ['R', 'U', 'D']:
            print("No")
            exit()

print("Yes")


# for i in range(len(S)):
#     if i % 2 == 0 and S[i] == "L":
#         print("No")
#         exit()
#     if i % 2 == 1 and S[i] == "R":
#         print("No")
#         exit()
# print("Yes")
