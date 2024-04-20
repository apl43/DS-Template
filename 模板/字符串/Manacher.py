def Manacher(s):
    s = "#" + "#".join(list(s)) + "#"
    n = len(s)
    d = [0] * n
    l, r = 0, -1
    for i in range(n):
        k = 1 if i > r else min(d[l + r - i], r - i + 1)
        while -1 < i - k and i + k < n and s[i - k] == s[i + k]:
            k += 1
        k -= 1
        d[i] = k
        if i + k > r:
            l = i - k
            r = i + k
    return d

print(Manacher("bcbabcc"))