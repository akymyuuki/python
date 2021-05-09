import collections

n, m = map(int, input().split())

Graph = [[] for i in range(n)]
isVisited = [False for i in range(n)]

for i in range(m):
    s,t = map(int, input().split())
    Graph[s].append(t)

out = collections.deque()

def dfs(u):
    isVisited[u] = True
    for v in Graph[u]:
        if not isVisited[v]:
            dfs(v)
    out.appendleft(u)

    
for s in range(n):
    if not isVisited[s]:
        dfs(s)

for i in range(len(out)):
    print(out[i])

