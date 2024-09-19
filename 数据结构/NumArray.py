class NumArray:
    def __init__(self, nums):
        n = len(nums)
        tree = [0] * (n + 1)
        for i, x in enumerate(nums, 1): # i 从 1 开始
            tree[i] += x
            nxt = i + (i & -i) # 下一个关键区间的右端点
            if nxt <= n:
                tree[nxt] += tree[i]
        self.nums = nums
        self.tree = tree

    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def prefixSum(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i &= i - 1
        return s

    def sumRange(self, left, right):
        return self.prefixSum(right + 1) - self.prefixSum(left)