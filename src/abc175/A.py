S = input()
c = S.count("R")
if c == 2:
    if S[1] != "R":
        c = 1

print(c)


# S = input()
# c = []
# r = 0
# for s in S:
#     if s == "R":
#         r += 1
#     else:
#         c.append(r)
#         r = 0

# c.append(r)

# print(max(c))
