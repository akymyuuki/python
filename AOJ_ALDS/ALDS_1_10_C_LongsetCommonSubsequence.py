N = 1000

def LCS(X, Y):
    C = [[-1 for i in range(N+1)] for j in range(N+1)]
    m = len(X)
    n = len(Y)
    maxL = 0
    X = ' ' + X
    Y = ' ' + Y
    for i in range(m+1):
        C[i][0] = 0
    for j in range(1, n+1):
        C[0][j] = 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i] == Y[j]:
                C[i][j] = C[i - 1][j -1] + 1
            else:
                C[i][j] = max(C[i - 1][j], C[i][j - 1])
            maxL = max(maxL, C[i][j])
    print(maxL)
    
def LCS_improved(X, Y):
    hist = [0]
    for c in Y:
        for i in range(len(hist)-1, -1, -1):
            next_match_index = X.find(c, hist[i])+1
            if next_match_index > 0:
                if i+1 < len(hist):
                    hist[i + 1] = min(hist[i+1], next_match_index)
                else:
                    hist.append(next_match_index)
    print(len(hist)-1)                
    
n = int(input())
for i in range(n):
    s1 = input()
    s2 = input()
    LCS_improved(s1, s2)

    
    