from collections import deque


n = edges = None


g = [[] for _ in range(n)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)


# 预处理祖先
# 求深度
m = n.bit_length()
pa = [[-1] * m for _ in range(n)]
depth = [0] * n
p = deque([(0, 0, -1)])
while p:
    x, d, fa = p.popleft()
    pa[x][0] = fa
    depth[x] = d
    for y in g[x]:
        if y != fa:
            p.append((y, d + 1, x))
# print(depth)

for i in range(m - 1):
    for x in range(n):
        p = pa[x][i]
        if p != -1:
            pp = pa[p][i]
            pa[x][i + 1] = pp
# print(pa)


# node 的 第 k 个 祖先
def get_kth_ancestor(node, k):
    for i in range(k.bit_length()):
        if (k >> i) & 1:
            node = pa[node][i]
    return node


def get_lca(x, y):
    if depth[x] > depth[y]:
        x, y = y, x
    y = get_kth_ancestor(y, depth[y] - depth[x])
    if x == y:
        return x
    for i in range(m - 1, -1, -1):
        px, py = pa[x][i], pa[y][i]
        if px != py:
            x, y = px, py
    return pa[x][0]


res = get_lca(x, y)