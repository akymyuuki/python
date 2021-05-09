import math


class Point:
    def __init__(self, v):
        self.v = v

    # ポイントに情報をセットする
    def setData(self, v):
        self.v = v

    # ポイントの情報を返す
    def getData(self):
        return self.v


class Graph:
    # n * n のグラフを作成する
    graph = []

    def __init__(self, n):
        self.graph = [[Point(0) for i in range(n)] for j in range(n)]

    def getPoint(self, x, y):
        return self.graph[x][y].getData()

    def setPoint(self, x, y, v):
        return self.graph[x][y].setData(v)


n = int(input())

graph = Graph(n)

for i in range(n - 1):
    a, b = map(int, input().split())
    graph.setPoint(a-1, b-1, 1)
    graph.setPoint(b-1, a-1, 1)

apple = []
for i in range(n):
    apple.append(int(input()))

print(apple[0])
appleCnt = 0
appleCnt += apple[0]
flag = True
i = 0
while flag:
    flag = False
    for j in range(n):
        if graph.getPoint(j, i) == 1:
            graph.setPoint(j, i, 0)
            graph.setPoint(i, j, 0)
            appleCnt += apple[j]
            print(appleCnt)
            i = j
            flag = True
