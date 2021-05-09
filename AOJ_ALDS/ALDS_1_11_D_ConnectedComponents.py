n,m = map(int,input().split())

G = [[] for i in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

C = [-1 for i in range(n)]
stack = []
cnt = 0
for i in range(n):
    if C[i] == -1:
        C[i] = cnt
        stack = [i]
        while stack:
            a = stack.pop()
            for j in G[a]:
                if C[j] == -1:
                    C[j] = cnt
                    stack.append(j)
        cnt += 1

nn = int(input())
for i in range(nn):
    s,t = map(int, input().split())
    if C[s] == C[t]:
        print('yes')
    else:
        print('no')

