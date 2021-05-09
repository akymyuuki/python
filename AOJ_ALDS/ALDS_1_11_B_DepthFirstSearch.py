n = int(input())

graph = [[0 for i in range(n)] for i in range(n)]
c = [0 for i in range(n)]
d = [0 for i in range(n)]
f = [0 for i in range(n)]
tt = 0

def dfs_visit(u):
    global tt
    c[u] = -1
    tt += 1
    d[u] = tt
    for i in range(n):
        if graph[u][i] == 0:
            continue
        if c[i] == 0:
            dfs_visit(i)
    c[u] = 1
    tt += 1
    f[u] = tt
    
def dfs():
    for i in range(n):
        if c[i] == 0:
            dfs_visit(i)
    for i in range(n):
        print(i+1, d[i], f[i])

for i in range(n):
    li = list(map(int, input().split()))
    m = li[1]
    for j in range(m):
        graph[i][li[j+2]-1] = 1

dfs()

