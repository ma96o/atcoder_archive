a = int(input())
b = int(input())
print([["EQUAL", "LESS"], ["GREATER"]][a > b][a < b])
# print("GREATER" if a > b else "LESS" if a < b else "EQUAL")
