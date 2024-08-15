class SegTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.sum = [0] * (2 << self.n.bit_length())
        self.min = [0] * (2 << self.n.bit_length())
        self.max = [0] * (2 << self.n.bit_length())
        self._build(self, 0, 0, self.n - 1)


    def _build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.max[o] = self.nums[l]
            return
        m = (l + r) // 2
        self._build(o * 2 + 1, l, m)
        self._build(o * 2 + 2, m + 1, r)
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])


    def add(self, idx: int, val: int) -> None:
        self._add(self, 0, 0, self.n - 1, idx, val)
    def _add(self, o: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.sum[o] += val
            self.min[o] += val
            self.max[o] += val
            return
        m = (l + r) // 2
        if idx <= m:
            self._add(o * 2 + 1, l, m, idx, val)
        else:
            self._add(o * 2 + 2, m + 1, r, idx, val)
        self.sum[o] = self.sum[o * 2 + 1] + self.sum[o * 2 + 2]
        self.min[o] = min(self.min[o * 2 + 1], self.min[o * 2 + 2])
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])
    

    # 更新单点sum
    def update_sum():...


    # 查找区间sum
    def query_sum(self, L: int, R: int) -> int:
        return self._query_sum(self, 0, 0, self.n - 1, L, R)
    def _query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res += self._query_sum(o * 2 + 1, l, m, L, R)
        if m < R:
            res += self._query_sum(o * 2 + 2, m + 1, r, L, R)
        return res


    # 更新单点min
    def update_min():...


    # 查找区间min
    def query_min(self, L: int, R: int) -> int:
        return self._query_min(self, 0, 0, self.n - 1, L, R)
    def _query_min(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.min[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = min(res, self._query_min(o * 2 + 1, l, m, L, R))
        if m < R:
            res = min(res, self._query_min(o * 2 + 2, m + 1, r, L, R))
        return res


    # 更新单点max
    def update_max(self, idx: int, val: int) -> None:
        self._update_max(self, 0, 0, self.n - 1, idx, val)
    def _update_max(self, o: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.nums[idx] = val
            self.max[o] = val
            return
        m = (l + r) // 2
        if idx <= m:
            self._update_max(o * 2 + 1, l, m, idx, val)
        else:
            self._update_max(o * 2 + 2, m + 1, r, idx, val)
        self.max[o] = max(self.max[o * 2 + 1], self.max[o * 2 + 2])


    # 查找区间max
    def query_max(self, L: int, R: int) -> int:
        return self._query_max(self, 0, 0, self.n - 1, L, R)
    def _query_max(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.max[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = max(res, self._query_max(o * 2 + 1, l, m, L, R))
        if m < R:
            res = max(res, self._query_max(o * 2 + 2, m + 1, r, L, R))
        return res


    # 返回 [L, R] 中 > val 的最小下标
    # 不存在就返回 -1
    def query1(self, L: int, R: int, val: int) -> int:
        return self._query1(self, 0, 0, self.n - 1, L, R, val)
    def _query1(self, o: int, l: int, r: int, L: int, R: int, val: int) -> int:
        if self.max[o] <= val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if L <= m:
            res_l = self._query1(o * 2 + 1, l, m, L, R, val)
            if res_l != -1:
                return res_l
        if m < R and self.max[o * 2 + 2] > val:
            res_r = self._query1(o * 2 + 2, m + 1, r, L, R, val)
            if res_r != -1:
                return res_r
        return -1


    # 返回 [L, R] 中 <= val 的最小下标
    # 不存在就返回 -1
    def query2(self, L: int, R: int, val: int) -> int:
        return self._query2(self, 0, 0, self.n - 1, L, R, val)
    def _query2(self, o: int, l: int, r: int, L: int, R: int, val: int) -> int:
        if self.min[o] > val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if L <= m:
            res_l = self._query2(o * 2 + 1, l, m, L, R, val)
            if res_l != -1:
                return res_l
        if m < R:
            res_r = self._query2(o * 2 + 1, m + 1, r, L, R, val)
            if res_r != -1:
                return res_r
        return -1