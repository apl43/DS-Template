class LazySegTree:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.sum = [0] * (2 << self.n.bit_length())
        self.sum_lazy = [0] * (2 << self.n.bit_length())
        self._build(0, 0, self.n - 1)


    def _build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.sum[o] = self.nums[l]
            return
        m = (l + r) // 2
        self._build(o * 2 + 1, l, m)
        self._build(o * 2 + 2, m + 1, r)
        self.sum[o] = self.sum[o * 2 + 1] + self.sum[o * 2 + 2]

    
    # 更新区间sum1 (区间 [l, r] 全部 ±val)
    def update_sum1(self, l: int, r: int, val: int) -> None:
        self._update_sum1(0, 0, self.n - 1, l, r, val)
    def _update_sum1(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None:
        if L <= l and r <= R:
            self.sum[o] += (r - l + 1) * val
            self.sum_lazy[o] += val
            return
        m = (l + r) // 2
        if self.sum_lazy[o] and l != r:
            x, self.sum_lazy[o] = self.sum_lazy[o], 0
            self.sum[o * 2 + 1] += x * (m - l + 1)
            self.sum[o * 2 + 2] += x * (r - m)
            self.sum_lazy[o * 2 + 1] += x
            self.sum_lazy[o * 2 + 2] += x
        if L <= m:
            self._update_sum1(o * 2 + 1, l, m, L, R, val)
        if m < R:
            self._update_sum1(o * 2 + 2, m + 1, r, L, R, val)
        self.sum[o] = self.sum[o * 2 + 1] + self.sum[o * 2 + 2]


    # 查找区间sum
    def query_sum(self, L: int, R: int) -> int:
        return self._query_sum(0, 0, self.n - 1, L, R)
    def _query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        m = (l + r) // 2
        if self.sum_lazy[o]:
            x, self.sum_lazy[o] = self.sum_lazy[o], 0
            self.sum[o * 2 + 1] += x * (m - l + 1)
            self.sum[o * 2 + 2] += x * (r - m)
            self.sum_lazy[o * 2 + 1] += x
            self.sum_lazy[o * 2 + 2] += x
        res = 0
        if L <= m:
            res += self._query_sum(o * 2 + 1, l, m, L, R)
        if m < R:
            res += self._query_sum(o * 2 + 2, m + 1, r, L, R)
        return res


    # 更新区间sum2 (区间 [l, r] 全部改为 val)
    def update_sum2(self, l: int, r: int, val: int) -> None:
        self._update_sum2(0, l, r, 0, self.n - 1, val)
    def _update_sum2(self, o: int, l: int, r: int, L: int, R: int, val: int) -> None: ...


    # 查找区间 (线段树上二分)
    def query(self, L: int, R: int, val: int) -> int:
        return self._query(0, 0, self.n - 1, L, R, val)
    def _query(self, o: int, l: int, r: int, L: int, R: int, val: int) -> int:
        if self.max[o] <= val:
            return -1
        if l == r:
            return l
        m = (l + r) // 2
        if self.sum_lazy[o]:
            x, self.sum_lazy[o] = self.sum_lazy[o], 0
            self.sum[o * 2 + 1] += x * (m - l + 1)
            self.sum[o * 2 + 2] += x * (r - m)
            self.sum_lazy[o * 2 + 1] += x
            self.sum_lazy[o * 2 + 2] += x
            x, self.max_lazy[o] = self.max_lazy[o], 0
            self.max[o * 2 + 1] += x
            self.max[o * 2 + 2] += x
            self.max_lazy[o * 2 + 1] += x
            self.max_lazy[o * 2 + 2] += x
        if L <= m:
            res_l = self._query(o * 2 + 1, l, m, L, R, val)
            if res_l != -1:
                return res_l
        if m < R and self.max[o * 2 + 2] > val:
            res_r = self._query(o * 2 + 2, m + 1, r, L, R, val)
            if res_r != -1:
                return res_r
        return -1


nums = [1, 5, 4, 2, 3]
n = len(nums)
g = LazySegTree(nums)


def p():
    print([g.query_sum(i, i) for i in range(n)])

p()
print(g.query_sum(1, 3))
g.update_sum1(1, 2, 2)
print(g.query_sum(2, 3))
g.update_sum1(0, 4, 1)
print(g.query_sum(0, 3))
