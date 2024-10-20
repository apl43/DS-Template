def kmp(text, pattern):
    # 求解 pi 数组
    m = len(pattern)
    pi = [0] * m
    st = 0
    for i in range(1, m):
        v = pattern[i]
        while st and pattern[st] != v:
            st = pi[st - 1]
        if pattern[st] == v:
            st += 1
        pi[i] = st
    
    st = 0
    res = []
    for i, v in enumerate(text):
        while st and pattern[st] != v:
            st = pi[st - 1]
        if pattern[st] == v:
            st += 1
        if st == m:
            res.append(i - m + 1)
            st = pi[st - 1]
    return res


print(kmp("abacabab", "abab"))
print(kmp([1, 2, 1, 3, 1, 2, 1, 2], [1, 2, 1, 2]))