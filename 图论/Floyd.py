from math import inf


n = None
edges = None


f = [[inf] * n for _ in range(n)]
for i in range(n):
    f[i][i] = 0
for x, y, w in edges:
    f[x][y] = w
    f[y][x] = w


for k in range(n):
    for i in range(n):
        for j in range(n):
            s = f[i][k] + f[k][j]
            if s < f[i][j]:
                f[i][j] = s


def add(x, y, w):
    if w >= f[x][y]:
        return
    for i in range(n):
        for j in range(n):
            if f[i][j] > f[i][x] + w + f[y][j]:
                f[i][j] = f[i][x] + w + f[y][j]


def find(start, end):
    return f[start][end] if f[start][end] != inf else -1