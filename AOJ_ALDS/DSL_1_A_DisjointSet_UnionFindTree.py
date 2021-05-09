n,m = map(int, input().split())

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
        
ds = DisjointSet(n)

for i in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        ds.unite(a, b)
    elif t == 1:
        if ds.same(a, b):
            print('1')
        else:
            print('0')
        