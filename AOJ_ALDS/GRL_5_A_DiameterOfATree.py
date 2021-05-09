import sys
from collections import deque
from enum import Enum
import sys
import math
from heapq import heappush, heappop
import copy

sys.setrecursionlimit(200000)

INF = 1 << 32

class Edge:
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist

V = int(input())
Graph = [[] for i in range(V)]

for i in range(V-1):
    from_, to_, dist_ = map(int, input().split())
    Graph[from_].append(Edge(to_, dist_))
    Graph[to_].append(Edge(from_, dist_))

ans = 0

def rec(id, parent):
    maxPath1 = 0
    maxPath2 = 0
    
    global ans
    
    for edge in Graph[id]:
        if edge.to == parent:
            continue
        tmp_dist = edge.dist + rec(edge.to, id)
        if tmp_dist > maxPath1:
            maxPath2 = maxPath1
            maxPath1 = tmp_dist
        elif tmp_dist > maxPath2:
            maxPath2 = tmp_dist
    
    ans = max(ans, maxPath1 + maxPath2)
    return maxPath1
    
rec(V//2, -1)
print(ans)