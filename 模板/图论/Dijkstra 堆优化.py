from math import inf
from heapq import *

n = None
edges = None

g = [[]for _ in range(n)]
for x, y, w in edges:
    g[x].append((y, w))
    g[y].append((x, w))


def add(x, y, w):
    g[x].append((y, w))
    g[y].append((x, w))

def find(start, end):
    dis = [inf] * n
    dis[start] = 0
    h = [(0, start)]
    while h:
        dx, x = heappop(h)
        if x == end:
            return dx   
        if dx > dis[x]:
            continue
        for y, w in g[x]:
            new_dis = dx + w
            if new_dis < dis[y]:
                dis[y] = new_dis
                heappush(h, (new_dis, y))
    return -1