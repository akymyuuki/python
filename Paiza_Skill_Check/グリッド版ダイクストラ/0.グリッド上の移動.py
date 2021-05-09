
h, w = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, 1, 0]
D = {'R': 0, 'U': 1, 'D': 2, 'L': 3}
move_list = ['R', 'D', 'R', 'U', 'L']

A = []

for i in range(h):
    A.append(list(map(int, input().split())))

sx = 0
sy = 0
cnt = 0
cnt += A[sy][sx]
for i in range(len(move_list)):
    sy += dy[D[move_list[i]]]
    sx += dx[D[move_list[i]]]
    cnt += A[sy][sx]

print(cnt)
