from collections import deque

n, m = map(int, input().split())

Graph = [[] for i in range(n)]
inDeg = [0 for i in range(n)]

for i in range(m):
    s,t = map(int, input().split())
    Graph[s].append(t)
    inDeg[t] +=1

Q = deque()

for i in range(n):
    if inDeg[i] == 0:
        Q.append(i)

out = deque()
def bfs():
    while len(Q) > 0:
        u = Q.pop()
        out.append(u)
        for a in Graph[u]:
            inDeg[a] -= 1
            if inDeg[a] == 0:
                Q.append(a)
    
bfs()

for i in range(len(out)):
    print(out[i])


