n = int(input())
G = [[0 for i in range(n)] for j in range(n)]
WHITE = 0
GRAY = 1
BLACK = 2
INF = 9999999999

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        G[i][j] = INF if li[j] == -1 else li[j]
        
def prim():
    u = 0
    minv = 9999999999;
    d = []
    p = []
    color = []
    
    for i in range(n):
        d.append(INF)
        p.append(-1)
        color.append(WHITE)
    
    d[0] = 0
    
    while True:
        minv = INF
        u = -1
        for i in range(n):
            if minv > d[i] and color[i] != BLACK:
                u = i
                minv = d[i]
        if u == -1:
            break
        color[u] = BLACK
        for v in range(n):
            if color[v] != BLACK and G[u][v] != INF:
                if d[v] > G[u][v]:
                    d[v] = G[u][v]
                    p[v] = u
                    color[v] = GRAY
    sumv = 0
    for i in range(n):
        if p[i] != -1:
            sumv += G[i][p[i]]
            
    print(sumv)
    
prim()
    
