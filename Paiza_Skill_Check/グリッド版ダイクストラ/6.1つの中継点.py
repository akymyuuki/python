import heapq


class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, state):
        return self.cost < state.cost

    def __hash__(self):
        return hash((self.x, self.y, self.cost))

    def __eq__(self, state):
        return self.x == state.x and \
            self.y == state.y and \
            self.cost == state.cost


def dijkstra(A, sx, sy, gx, gy):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    oq = []
    cq = set()
    state = State(sx, sy, A[sy][sx])
    heapq.heappush(oq, state)
    while len(oq) > 0:
        state = heapq.heappop(oq)
        if state.x == gx and state.y == gy:
            return state.cost
        if state in cq:
            continue
        cq.add(state)
        for i in range(4):
            nx = state.x + dx[i]
            ny = state.y + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            ncost = state.cost + A[ny][nx]
            heapq.heappush(oq, State(nx, ny, ncost))


h, w = map(int, input().split())

A = [[0 for i in range(w)] for j in range(h)]


for i in range(h):
    l = list(map(int, input().split()))
    for j in range(w):
        A[i][j] = l[j]

ans1 = dijkstra(A, 0, 0, w-1, 0)
ans2 = dijkstra(A, w-1, 0, w-1, h-1)
print(ans1+ans2-A[0][w-1])
