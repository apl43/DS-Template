MX = 10 ** 6
LPF = [0] * MX
for i in range(2, MX):
    if LPF[i]:
        continue
    for j in range(i, MX, i):
        if LPF[j] == 0:
            LPF[j] = i
            
# print(LPF)