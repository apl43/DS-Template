"""
a^b, 模是 m

if gcd(a, m) == 1: a^b = a^(b % phi(m)) % m

elif b < phi(m):   a^b = a^b % m

else:              a^b = a^(b % phi(m) + phi(m)) % m

"""

# phi(n) 表示小于等于 n 和 n 互质的数的个数
# 如果 n 为质数，phi(n) = n - 1

def phi(x):
    res = x
    i = 2
    while i * i <= x:
        if x % i == 0:
            res = res // i * (i - 1)
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        res = res // x * (x - 1)
    return res