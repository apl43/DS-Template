class BIT:
    def __init__(self, nums):
        n = len(nums)
        self.g = [0] * (n + 1)
        for i, x in enumerate(nums, 1): # i 从 1 开始
            self.g[i] += x
            nxt = i + (i & -i) # 下一个关键区间的右端点
            if nxt <= n:
                self.g[nxt] += self.g[i]


    # 单点更新
    def update(self, idx, val):
        i = idx + 1
        while i < len(self.g):
            self.g[i] += val
            i += i & -i


    # 计算前缀和
    def prefix_sum(self, i: int) -> int:
        s = 0
        while i:
            s += self.g[i]
            i &= i - 1
        return s


    # 查找区间sum
    def query_sum(self, l: int, r: int) -> int:
        return self.prefix_sum(r + 1) - self.prefix_sum(l)
    

g = BIT([1] * 5)

print(g.prefix_sum(0))
print(g.prefix_sum(1))