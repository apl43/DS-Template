"""
a^b, 模是 m

if gcd(a, m) == 1: a^b = a^(b % phi(m)) % m

elif b < phi(m):   a^b = a^b % m

else:              a^b = a^(b % phi(m) + phi(m)) % m

"""

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