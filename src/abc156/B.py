N, K = map(int, input().split())


def base_10_t0_n(x, n):
    if(int(x/n)):
        return base_10_t0_n(int(x/n), n)+str(x % n)
    return str(x % n)


NK = base_10_t0_n(N, K)
print(len(NK))


# print(int(math.log(N, K)+1))

# S = ""
# while N > 0:
#     S = S + str(N % K)
#     N = N // K

# print(len(S))
