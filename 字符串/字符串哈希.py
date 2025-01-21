class Hash:
    def __init__(self, s, BASE=13331, MOD=10**9+7):
        self.n = len(s)
        self.BASE = BASE
        self.MOD = MOD
        self.pre = [0]
        self.pw = [1]
        for x in s:
            self.pre.append((self.pre[-1] * BASE % MOD + ord(x) - ord("a")) % MOD)
            self.pw.append(self.pw[-1] * BASE % MOD)

    def get(self, l, r):
        return (self.pre[r + 1] - self.pre[l] * self.pw[r + 1 - l] % self.MOD) % self.MOD


