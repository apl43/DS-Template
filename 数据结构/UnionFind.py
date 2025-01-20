class UnionFind:
    def __init__(self, size):
        self.fa = list(range(size))
    
    def find(self, x):
        # # 递归方式
        # if self.fa[x] != x:
        #     self.fa[x] = self.find(self.fa[x])
        # return self.fa[x]
        
        # 非递归方式
        y = x
        while self.fa[y] != y:
            y = self.fa[y]
        
        while self.fa[x] != y:
            x = self.fa[x]
            self.fa[x] = y
        return self.fa[y]
        
    def union(self, x, y): # x 连接到 y 上
        self.fa[self.find(x)] = self.find(y)


class UnionFind:
    def __init__(self, size):
        self.fa = list(range(size))
        self.size = [1] * size
    
    def find(self, x):
        y = x
        while self.fa[y] != y:
            y = self.fa[y]
        
        while self.fa[x] != y:
            x = self.fa[x]
            self.fa[x] = y
        return self.fa[y]
        
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.fa[y] = x
        self.size[x] += self.size[y]