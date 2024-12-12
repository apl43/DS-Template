"""
a^b, 模是 m

if gcd(a, m) == 1: a^b = a^(b % phi(m)) % m

elif b < phi(m):   a^b = a^b % m

else:              a^b = a^(b % phi(m) + phi(m)) % m

"""

# phi(n) 表示小于等于 n 和 n 互质的数的个数
# 如果 n 为质数，phi(n) = n - 1

def phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res = res // i * (i - 1)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res