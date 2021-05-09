class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


def preParse(u):
    if u == -1:
        return
    printArr.append((" " + str(u)))
    preParse(node[u].left)
    preParse(node[u].right)


def inParse(u):
    if u == -1:
        return
    inParse(node[u].left)
    printArr.append((" " + str(u)))
    inParse(node[u].right)


def postParse(u):
    if u == -1:
        return
    postParse(node[u].left)
    postParse(node[u].right)
    printArr.append((" " + str(u)))


n = int(input())
node = [Node(-1, -1, -1) for i in range(n)]

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

printArr = []
print("Preorder")
preParse(r)
print(''.join(printArr))

printArr = []
print("Inorder")
inParse(r)
print(''.join(printArr))

printArr = []
print("Postorder")
postParse(r)
print(''.join(printArr))
