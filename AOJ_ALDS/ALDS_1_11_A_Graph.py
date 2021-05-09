n = int(input())

graph = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    li = list(map(int, input().split()))
    m = li[1]
    for j in range(m):
        graph[i][li[j+2]-1] = 1
        
for i in range(n):
    s = ' '.join(map(str, graph[i]))
    print(s)