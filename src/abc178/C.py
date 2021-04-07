N = int(input())

print((10**N - 9**N*2 + 8**N) % (10**9+7))

# MOD = 10**9+7
# print((pow(10, N, MOD) - 2*pow(9, N, MOD) + pow(8, N, MOD)) % MOD)
