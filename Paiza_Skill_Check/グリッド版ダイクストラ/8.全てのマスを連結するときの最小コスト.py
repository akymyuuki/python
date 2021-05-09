import heapq


class State:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, state):
        return self.cost < state.cost

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, state):
        return self.x == state.x and \
            self.y == state.y


def dijkstra(A, sx, sy):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    oq = []
    cq = set()
    cost = 0
    state = State(sx, sy, 0)
    heapq.heappush(oq, state)
    while len(oq) > 0:
        state = heapq.heappop(oq)
        if state in cq:
            continue
        cq.add(state)
        cost += state.cost
        if len(cq) == w * h:
            return cost
        for i in range(4):
            nx = state.x + dx[i]
            ny = state.y + dy[i]
            if nx < 0 or w <= nx or ny < 0 or h <= ny:
                continue
            ncost = A[state.y][state.x] * A[ny][nx]
            heapq.heappush(oq, State(nx, ny, ncost))


h, w = map(int, input().split())

A = [[0 for i in range(w)] for j in range(h)]


for i in range(h):
    l = list(map(int, input().split()))
    for j in range(w):
        A[i][j] = l[j]

ans = dijkstra(A, 0, 0)
print(ans)
