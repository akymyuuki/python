class Node:
    def __init__(self, parent, leaf, depth):
        self.parent = parent
        self.leaf = leaf
        self.depth = depth


def rec(u, d):
    node[u].depth = d
    for i in range(len(node[u].leaf)):
        rec(node[u].leaf[i], d + 1)


def printNode(r, an):
    printStr = ""
    printStr += "node " + str(r) + ": "
    printStr += "parent = " + str(an.parent) + ", "
    printStr += "depth = " + str(an.depth) + ", "
    if an.parent == -1:
        printStr += "root, [" + ', '.join(map(str, an.leaf)) + "]"
    elif len(an.leaf) == 0:
        printStr += "leaf, [" + ', '.join(map(str, an.leaf)) + "]"
    else:
        printStr += "internal node, [" + ', '.join(map(str, an.leaf)) + "]"
    print(printStr)


n = int(input())
node = [Node(-1, [], -1) for i in range(n)]

for i in range(n):
    l = list(map(int, input().split()))
    for i in range(2, len(l)):
        node[l[0]].leaf.append(l[i])
        node[l[i]].parent = l[0]
r = -1
for i in range(n):
    if node[i].parent == -1:
        r = i
rec(r, 0)
for i in range(n):
    printNode(i, node[i])
