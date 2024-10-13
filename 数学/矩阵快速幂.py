MOD = 10 ** 9 + 7


def multiply_matrices(e, p):
    n, m, l = len(e), len(p[0]), len(e[0])
    res = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(l):
                res[i][j] += e[i][k] * p[k][j]
                res[i][j] %= MOD
    return res

f = None
base = None
k = None

while k:
    if k & 1:
        f = multiply_matrices(f, base)
    base = multiply_matrices(base, base)
    k >>= 1

print()