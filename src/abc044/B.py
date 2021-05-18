import collections
w = input()
for v in collections.Counter(w).values():
    if v % 2 != 0:
        print("No")
        exit()

print("Yes")
