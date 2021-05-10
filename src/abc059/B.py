a = int(input())
b = int(input())
print([["EQUAL", "LESS"], ["GREATER"]][a > b][a < b])
