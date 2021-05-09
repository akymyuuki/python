n = int(input())

graph = [[0 for i in range(n)] for i in range(n)]
d = [9999999999 for i in range(n)]

q = []
qt = []

def bfs():
    q.append(0)
    qt.append(0)
    while len(q) > 0:
        a = q.pop(0)
        t = qt.pop(0)
        d[a] = min(d[a], t)
        for i in range(n):
            if graph[a][i] == 1:
                q.append(i)
                qt.append(t+1)
                graph[a][i] = 0
                
for i in range(n):
    li = list(map(int, input().split()))
    m = li[1]
    for j in range(m):
        graph[i][li[j+2]-1] = 1

bfs()

for i in range(n):
    if d[i] == 9999999999:
        print(i+1, -1)
    else:
        print(i+1, d[i])

