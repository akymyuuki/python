INF = 1 << 32
V, E = map(int, input().split())

Graph = [[INF for i in range(V)] for j in range(V)]

for i in range(E):
    s,t,c = map(int, input().split())
    Graph[s][t] = c

for i in range(V):
    Graph[i][i] = 0

def warshallFloyd():
    for mid in range(V):
        for start in range(V):
            if Graph[start][mid] == INF:
                continue
            for goal in range(V):
                if Graph[mid][goal] == INF:
                    continue
                Graph[start][goal] = min(Graph[start][goal], Graph[start][mid]+ Graph[mid][goal])

warshallFloyd()

negative = False
for i in range(V):
    if Graph[i][i] < 0:
        negative = True

if negative:
    print('NEGATIVE CYCLE')
else:
    for i in range(V):
        for j in range(V):
            if j > 0:
                print(' ', end="")
            if Graph[i][j] == INF:
                print('INF', end="")
            else:
                print(Graph[i][j], end="")
        print()
    