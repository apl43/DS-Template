class Factorial:
    def __init__(self, MX, MOD):
        # i 的阶乘
        fac = [1] * MX
        for i in range(1, MX):
            fac[i] = fac[i - 1] * i % MOD
        # i 的阶乘的逆元
        inv_fac = [0] * MX
        inv_fac[-1] = pow(fac[-1], -1, MOD)
        for i in range(MX - 2, -1, -1):
            inv_fac[i] = inv_fac[i + 1] * (i + 1) % MOD
        self.fac, self.inv_fac, self.MOD = fac, inv_fac, MOD

    def comb(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        return self.fac[n] * self.inv_fac[k] % self.MOD * self.inv_fac[n - k] % self.MOD

    # 排列: 从 n 个不同元素中取出 k 个元素 (k <= n)
    def perm(self, n, k):
        if n < 0 or k < 0 or n < k:
            return 0
        return self.fac[n] * self.inv_fac[n - k] % self.MOD

    # 卡特兰数1
    # 0 1 2 3 4  5  6   7
    # 1 1 2 5 14 42 132 429
    def catalan1(self, n):
        return (self.comb(2 * n, n) - self.comb(2 * n, n - 1)) % self.MOD
    
    # 卡特兰数2 (n <= k)
    # 1
    # 1 1
    # 1 2 2
    # 1 3 5 5
    # 1 4 9 14 14
    def catalan2(self, n, k):
        return self.fac[n + k] * (n - k + 1) % self.MOD * self.inv_fac[k] % self.MOD * self.inv_fac[n + 1] % self.MOD

    # 第二类斯特林数 将 n 个两两不同的元素，划分为 k 个互不区分的非空子集的方案数
    def stirling(self, n, k): ...



F = Factorial(200050, 10 ** 9 + 7)
