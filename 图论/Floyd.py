from math import inf


n = None
edges = None


g = [[inf] * n for _ in range(n)]
for i in range(n):
    g[i][i] = 0
for x, y, w in edges:
    g[x][y] = w
    g[y][x] = w


for k in range(n):
    for i in range(n):
        for j in range(n):
            s = g[i][k] + g[k][j]
            if s < g[i][j]:
                g[i][j] = s


def add(x, y, w):
    if w >= g[x][y]:
        return
    for i in range(n):
        for j in range(n):
            if g[i][j] > g[i][x] + w + g[y][j]:
                g[i][j] = g[i][x] + w + g[y][j]


def find(start, end):
    return g[start][end] if g[start][end] != inf else -1