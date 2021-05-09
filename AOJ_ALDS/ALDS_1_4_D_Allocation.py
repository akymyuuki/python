import math
n,k = map(int, input().split())

# 最大積載量Pのk台のトラックで何個の荷物を積めるか？
def check(p):
    i = 0
    for j in range(k):
        S = 0
        while S + T[i] <= p:
            S += T[i]
            i += 1
            if i == n:
                return n
    return i

def solve():
    left = 0
    right = 100000 * 10000
    mid = 0
    while right - left > 1:
        mid = math.floor((left + right) / 2)
        v = check(mid) # mid == Pを決めて何個積めるかチェック
        if v >= n:
            right = mid
        else:
            left = mid
    return right


T = list()
for i in range(n):    
    T.append(int(input()))

ans = solve()
print(ans)