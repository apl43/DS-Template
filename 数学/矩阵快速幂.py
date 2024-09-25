MOD = 10 ** 9 + 7
n, k = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

def f(x, y):
    n = len(x)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += x[i][k] * y[k][j]
                res[i][j] %= MOD
    return res

ans = [[0] * n for _ in range(n)]
for i in range(n):
    ans[i][i] = 1

while k:
    if k & 1:
        ans = f(ans, g)
    g = f(g, g)
    k >>= 1
for row in ans:
    print(" ".join(map(str, row)))