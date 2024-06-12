class SegTree:
    def __init__(self, nums):
        self.nums = nums
        n = len(nums)
        self.sum = [0] * (2 << n.bit_length())
        self.min = [0] * (2 << n.bit_length())
        self.max = [0] * (2 << n.bit_length())


    def build(self, o, l, r):
        if l == r:
            self.max[o] = self.nums[l]
            return
        m = (l + r) // 2
        self.build(o * 2 + 1, l, m)
        self.build(o * 2 + 2, m + 1, r)
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])


    def add(self, o, l, r, idx, val):
        if l == r:
            self.sum[o] += val
            self.min[o] += val
            self.max[o] += val
            return
        m = (l + r) // 2
        if idx <= m:
            self.add(o * 2 + 1, l, m, idx, val)
        else:
            self.add(o * 2 + 2, m + 1, r, idx, val)
        self.sum[o] = self.sum[o * 2 + 1] + self.sum[o * 2 + 2]
        self.min[o] = min(self.min[o * 2 + 1], self.min[o * 2 + 2])
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])
    
    # 区间sum
    def query_sum(self, o, l, r, L, R):
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res += self.query_sum(o * 2 + 1, l, m, L, R)
        if m < R:
            res += self.query_sum(o * 2 + 2, m + 1, r, L, R)
        return res


    # 区间min
    def query_min(self, o, l, r, idx, val):
        pass


    # 更新区间max
    def update_max(self, o, l, r, idx, val):
        if l == r:
            self.nums[idx] = val
            self.max[o] = val
            return
        m = (l + r) // 2
        if idx <= m:
            self.update_max(o * 2 + 1, l, m, idx, val)
        else:
            self.update_max(o * 2 + 2, m + 1, r, idx, val)
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])


    # 区间max
    def query_max(self, o, l, r, L, R):
        if L <= l and r <= R:
            return self.max[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = max(res, self.query_max(o * 2 + 1, l, m, L, R))
        if m < R:
            res = max(res, self.query_max(o * 2 + 2, m + 1, r, L, R))
        return res


    # 返回 [L, R] 中 > val 的最小下标
    # 不存在就返回 -1
    def query1(self, o, l, r, L, R, val):
        if self.max[o] <= val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if L <= m:
            res_l = self.query1(o * 2 + 1, l, m, L, R, val)
            if res_l != -1:
                return res_l
        if m < R and self.max[o * 2 + 2] > val:
            res_r = self.query1(o * 2 + 2, m + 1, r, L, R, val)
            if res_r != -1:
                return res_r
        return -1


    # 返回 [L, R] 中 <= val 的最小下标
    # 不存在就返回 -1
    def query2(self, o, l, r, L, R, val):
        if self.min[o] > val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if L <= m:
            res_l = self.query2(o * 2 + 1, l, m, L, R, val)
            if res_l != -1:
                return res_l
        if m < R:
            res_r = self.query2(o * 2 + 1, m + 1, r, L, R, val)
            if res_r != -1:
                return res_r
        return -1