import sys

sys.setrecursionlimit(200000)

n, m = map(int, input().split())

E = [set() for i in range(n)]

for i in range(m):
    s,t = map(int, input().split())
    E[s].add(t)
    E[t].add(s)
    
prenum = [None for i in range(n)]
parent = [None for i in range(n)]
lowest = [None for i in range(n)]
cnt = 0

def dfs(cur, prev):
    global cnt
    prenum[cur] = cnt
    lowest[cur] = cnt
    cnt += 1
    for e in E[cur]:
        if prenum[e] is not None:
            if e != prev:
                lowest[cur] = min(lowest[cur], prenum[e])
            continue
        parent[e] = cur
        dfs(e, cur)
        lowest[cur] = min(lowest[cur], lowest[e])
        
dfs(0, 1)
ap = [False for i in range(n)]
r = 0
for i in filter(lambda x: x == 0, parent):
    r += 1
    if r > 1:
        ap[0] = True
        break
    
for i in range(1, n):
    p = parent[i]
    if p and prenum[p] <= lowest[i]:
        ap[p] = True
        
for i, e in enumerate(ap):
    if e: print(i)
