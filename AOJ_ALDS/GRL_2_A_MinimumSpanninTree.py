class DisjointSet:
    p = []
    rank = []
    def __init__(self, n):
        self.p = [0 for i in range(n)]
        self.rank = [0 for i in range(n)]
        for i in range(n):
            self.makeSet(i)
    
    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0
        
    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)
        
    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))
    
    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            
    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

class Edge:
    def __init__(self, source, target, cost):
        self.source = source
        self.target = target
        self.cost = cost
    def __lt__(self, arg):
        return self.cost < arg.cost

def kruskal():
    totalCost = 0
    edges.sort()
    ds = DisjointSet(n+1)
    
    for i in range(n):
        ds.makeSet(i)
    
    for i in range(len(edges)):
        e = edges[i]
        if not ds.same(e.source, e.target):
            totalCost += e.cost
            ds.unite(e.source, e.target)
    return totalCost
    
n,m = map(int, input().split())


edges = []

for i in range(m):
    s,t,c = map(int, input().split())
    edges.append(Edge(s,t,c))
    
ans = kruskal()

print(ans)