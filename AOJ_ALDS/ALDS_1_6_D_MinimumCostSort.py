def solve(n, A, s):
    VMAX = 10000
    ans = 0
    B = sorted(A)
    T = [-1 for i in range(VMAX + 1)]
    V = [False for i in range(n)]
    for i in range(n):
        T[B[i]] = i
    for i in range(n):
        if(V[i]):
            continue
        cur = i
        S = 0
        m = VMAX
        an = 0
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
            if V[cur]:
                break
        ans += min(S + (an - 2) * m, m + S + (an + 1) * s)
    return ans


n = int(input())
A = list(map(int, input().split()))

ans = solve(n, A, min(A))

print(ans)
