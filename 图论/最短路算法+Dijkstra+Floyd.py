from math import inf

"""
Dijkstra （加多查少）
从起点开始， 一直选择最短路（权值最小的路）， 直到找到终点， 或所有点都走完
优点： 每次添加点都是 O(1)
缺点： 每次查找都是 O(n ^ 2)

Floyd （查多加少）
优点： 每次查找都是 O(1)
缺点： 预处理需要大量时间， 添加一条边需要 O(n ^ 2)
"""
class Graph:
    def __init__(self, n: int, edges: list[list[int]]):
        g = [[inf] * n for _ in range(n)]
        for x, y, w in edges:
            g[x][y] = w
            # g[y][x] = w
        self.g = g
    
    def Dijkstra_add(self, e: list[int]) -> None:
        self.g[e[0]][e[1]] = e[2]

    # 时间复杂度 O(n ^ 2)
    def Dijkstra_find(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [inf] * n # start 到所有点的最短路
        dis[start] = 0 # 只有 dis[start] 为 0， 其余为 inf， 在一开始的循环只会找到 start
        vis = [False] * n # 标记已经被更新成最短路的点
        while True:
            x = -1 # 下一个要走的点
            for i in range(n):
                # 在 vis[i] 没有被更新成最短路的点的前提下， 找到最短的下一步， 将下标赋值给 x
                if not vis[i] and (x < 0 or dis[i] < dis[x]): 
                    x = i
            # 如果所有点都更新完了也还没找到 end
            # 或者下一步无法走到下一步 dis[x] == inf（图不是连通图）
            if x < 0 or dis[x] == inf:
                return -1
            if x == end: # 找到 end 之后必定是最短的
                return dis[x]
            # 更新， 之后不会再循环到 dis[x]
            vis[x] = True
            for y, w in enumerate(self.g[x]): 
                # 取最短路， dis[y] == inf 时直接被更新
                # dis[y] = min(dis[y], dis[x] + w)
                if dis[x] + w < dis[y]:
                    dis[y] = dis[x] + w
            
    # Floyd 算法的预处理
    def Floyd_pretreatment(self):
        g = self.g
        n = len(g)
        for i in range(n):
            g[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    s = g[i][k] + g[k][j]
                    if s < g[i][j]:
                        g[i][j] = s

    # 时间复杂度 O(n ^ 2)
    def Floyd_add(self, e: list[int]) -> None:
        g = self.g
        n = len(g)
        x, y, w = e
        if w >= g[x][y]:
            return 
        g[x][y] = w
        for i in range(n):
            for j in range(n):
                s = g[i][x] + g[x][y] + g[y][j]
                if s < g[i][j]:
                    g[i][j] = s

    def Floyd_find(self, start: int, end: int) -> int:
        dis = self.g[start][end]
        return dis if dis < inf else -1


"""
使用方法

n = 节点个数
edges = [[start, end, weight], [start, end, weight], [start, end, weight], ...]

obj = Graph(n, edges)
# obj.Floyd_pretreatment()  使用 Floyd 算法时需要


添加一条边
obj.Dijkstra_add([start, end, weight])
obj.Floyd_add([start, end, weight])

查找最短路
obj.Dijkstra_find(start, end)
obj.Floyd_find(start, end)
"""


obj = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])

print(obj.Dijkstra_find(3, 2))
# print(obj.Dijkstra_find(0, 3))
# print(obj.Dijkstra_add([1, 3, 4]))
# print(obj.Dijkstra_find(0, 3))

# obj.Floyd_pretreatment()
# print(obj.Floyd_find(3, 2))
# print(obj.Floyd_find(0, 3))
# print(obj.Floyd_add([1, 3, 4]))
# print(obj.Floyd_find(0, 3))

