# 欧拉筛
n = 1000000
pri = []
prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, n + 1):
    if prime[i]:
        pri.append(i)
    for pri_j in pri:
        if i * pri_j > n:
            break
        prime[i * pri_j] = False
        if i % pri_j == 0:
            break


# 埃氏筛
