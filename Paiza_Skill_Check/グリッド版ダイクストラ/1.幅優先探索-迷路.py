
h, w = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

A = [[1 for i in range(w+2)] for j in range(h+2)]

for i in range(h):
    l = (list(map(int, input().split())))
    for j in range(w):
        A[i+1][j+1] = l[j]

xq = []
yq = []
cntq = []
xq.append(1)
yq.append(1)
cntq.append(0)
sx = 1
sy = 1
cnt = 1
while len(xq) > 0:
    sx = xq.pop(0)
    sy = yq.pop(0)
    cnt = cntq.pop(0)
    A[sy][sx] = 1
    if sx == w and sy == h:
        cnt += 1
        break
    for i in range(4):
        if A[sy+dy[i]][sx+dx[i]] == 0:
            xq.append(sx+dx[i])
            yq.append(sy+dy[i])
            cntq.append(cnt+1)

print(cnt)
