import math
n = int(input())
# mod 7 で配列に格納するため、配列の長さは7
a = [0 for i in range(7)]

# %で割ったあまりに応じて配列に格納していく
for i in range(n):
    ln = int(input())
    a[ln % 7] += 1

# 合計を記録する。他の言語では桁あふれに注意
cnt = 0

#
for i in range(7):
    for j in range(i, 7):
        for k in range(j, 7):
            if (i+j+k) % 7 == 0:
                n1, n2, n3 = a[i], a[j], a[k]
                if i == j:
                    n2 -= 1
                if i == k:
                    n3 -= 1
                if j == k:
                    n3 -= 1
                b = (n1 * n2 * n3)
                if i == 0 and j == 0 and k == 0:
                    b /= 6
                elif i == j or j == k or i == k:
                    b /= 2
                cnt += math.floor(b)
print(cnt)
