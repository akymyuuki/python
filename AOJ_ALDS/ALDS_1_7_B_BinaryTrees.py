class Node:
    def __init__(self, parent, left, right, depth, height):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.height = height


def setDepth(u, d):
    if u == -1:
        return
    node[u].depth = d
    setDepth(node[u].left, d + 1)
    setDepth(node[u].right, d + 1)


def setHeight(u):
    h1 = 0
    h2 = 0
    if node[u].left != -1:
        h1 = setHeight(node[u].left) + 1
    if node[u].right != -1:
        h2 = setHeight(node[u].right) + 1
    node[u].height = h1 if h1 > h2 else h2
    return node[u].height


def getSibling(u):
    if node[u].parent == -1:
        return -1
    p = node[u].parent
    if node[p].left != u and node[p].left != -1:
        return node[p].left
    if node[p].right != u and node[p].right != -1:
        return node[p].right
    return -1


def printNode(r, an):
    printStr = ""
    printStr += "node " + str(r) + ": "
    printStr += "parent = " + str(an.parent) + ", "
    printStr += "sibling = " + str(getSibling(r)) + ", "
    deg = 0
    if an.left != -1:
        deg += 1
    if an.right != -1:
        deg += 1
    printStr += "degree = " + str(deg) + ", "
    printStr += "depth = " + str(an.depth) + ", "
    printStr += "height = " + str(an.height) + ", "
    if an.parent == -1:
        printStr += "root"
    elif an.left == -1 and an.right == -1:
        printStr += "leaf"
    else:
        printStr += "internal node"
    print(printStr)


n = int(input())
node = [Node(-1, -1, -1, -1, -1) for i in range(n)]

for i in range(n):
    v, left, right = list(map(int, input().split()))
    node[v].left = left
    node[v].right = right
    if left != -1:
        node[left].parent = v
    if right != -1:
        node[right].parent = v

r = 0
for i in range(n):
    if node[i].parent == -1:
        r = i

setDepth(r, 0)
setHeight(r)

for i in range(n):
    printNode(i, node[i])
