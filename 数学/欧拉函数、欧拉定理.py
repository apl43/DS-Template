"""
a^b, 模是 m

if gcd(a, m) == 1: a^b = a^(b % phi(m)) % m

elif b < phi(m):   a^b = a^b % m

else:              a^b = a^(b % phi(m) + phi(m)) % m

"""

# phi(n) 表示小于等于 n 和 n 互质的数的个数
# 如果 n 为质数，phi(n) = n - 1

def phi(x):
    s = x
    if x == 1:
        return 1
    c = set()
    for i in range(2, x):
        while x % i == 0:
            c.add(i)
            x //= i
    if x > 1:
        c.add(x)
    for y in c:
        s *= y - 1
        s //= y
    return s