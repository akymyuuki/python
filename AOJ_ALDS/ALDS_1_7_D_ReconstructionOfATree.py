class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


def poio_node(node, po, io):
    root = po[0]
    i = io.index(root)
    if i != 0:
        node[po[0]].left = po[1]
        node[po[1]].parent = po[0]
        poio_node(node, po[1:i+1], io[:i])
    if i != len(io) - 1:
        node[po[0]].right = po[i+1]
        node[po[i+1]].parent = po[0]
        poio_node(node, po[i+1:], io[i+1:])


def postOrder(node, i):
    if node[i].left != -1:
        postOrder(node, node[i].left)
    if node[i].right != -1:
        postOrder(node, node[i].right)
    post.append(str(i+1))


def minus1(n):
    return (n-1)


n = int(input())
po = list(map(int, input().split()))
io = list(map(int, input().split()))
po = list(map(minus1, po))
io = list(map(minus1, io))
node = [Node(-1, -1, -1) for i in range(n)]

poio_node(node, po, io)

post = []
postOrder(node, po[0])
print(' '.join(post))
