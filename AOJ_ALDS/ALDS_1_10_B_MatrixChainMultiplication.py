
def matrixChainMultiplication(n):
    m = [[0 for i in range(n+1)] for j in range(n+1)]
    for l in range(2, n+1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = 999999999 
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j])
    print(m[1][n])
    

n = int(input())
p = []

for i in range(n):
    li = input().split()
    p.append(int(li[0]))
p.append(int(li[1]))

matrixChainMultiplication(n)