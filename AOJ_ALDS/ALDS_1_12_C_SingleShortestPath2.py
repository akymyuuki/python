from queue import PriorityQueue
WHITE = 0
GRAY = 1
BLACK = 2
INF = 1<<30

n = int(input())

Graph = [[] for i in range(n+1)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(0,li[1]*2, 2):
        Graph[li[0]].append((li[j+2],li[j+3]))


def dijkstra():
    PQ = PriorityQueue()
    d = [INF for i in range(n)]
    color = [WHITE for i in range(n)]
    
    d[0] = 0
    PQ.put((0, 0))
    while not PQ.empty():
        f = PQ.get()
        u = f[1]
        
        color[u] = BLACK
        
        lens = len(Graph[u])
        for j in range(lens):
            v = Graph[u][j][0]
            if color[v] != BLACK and d[v] > d[u] + Graph[u][j][1]:
                d[v] = d[u] + Graph[u][j][1]
                PQ.put((d[v], v))
    

    for i in range(n):
        print(i, -1 if d[i] == INF else d[i])


dijkstra()