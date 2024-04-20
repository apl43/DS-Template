from math import inf

n = None
edges = None

g = [[inf] * n for _ in range(n)]
for x, y, w in edges:
    g[x][y] = w
    # g[y][x] = w

def add(x, y, w):
    g[x][y] = w
    # g[y][x] = w

def find(start, end):
    dis = [inf] * n
    dis[start] = 0
    vis = [False] * n
    while True:
        x = -1
        for i in range(n):
            if not vis[i] and (x < 0 or dis[i] < dis[x]):
                x = i
        if x < 0 or dis[x] == inf:
            return -1
        if x == end:
            return dis[x]
        vis[x] = True
        for y, w in enumerate(g[x]):
            dis[y] = min(dis[y], dis[x] + w)