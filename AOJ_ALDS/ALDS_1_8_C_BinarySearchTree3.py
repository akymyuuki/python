import sys
input = sys.stdin.readline

NIL = -1

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def show_keys(self):
        in_order(self.root)
        print('')
        pre_order(self.root)
        print('')
    def insert_key(self, key):
        node = Node(key)
        insert_node(self, node)
    def find_key(self, key):
        if find_node(self.root, key):
            print('yes')
        else:
            print('no')
    def delete_key(self, key):
        node = find_node(self.root, key)
        delete_node(self, node)
        
class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def insert_node(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def delete_node(T, node):
    if node.left and node.right:
        x = node.right
        while x.left:
            x = x.left
        node.key = x.key
        delete_node(T, x)
    elif node.left or node.right:
        child = node.left or node.right
        if node is T.root:
            T.root = child
            child.parent = None
        else:
            if node.parent.left is node:
                node.parent.left = child
                child.parent = node.parent
            else:
                node.parent.right = child
                child.parent = node.parent
    else:
        if node.parent.left is node:
            node.parent.left = None
        else:
            node.parent.right = None

def in_order(node):
    if node:
        in_order(node.left)
        print(" " + str(node.key), end = '')
        in_order(node.right)
        
def pre_order(node):
    if node:
        print(" " + str(node.key), end = '')
        pre_order(node.left)
        pre_order(node.right)

def find_node(node, k):
    while node:
        if node.key == k:
            return node
        if k < node.key:
            node = node.left
        else:
            node = node.right

n = int(input())
T = BinarySearchTree()

Order = []
for i in range(n):
    l = input().split()
    Order.append(l)

for l in Order:
    if l[0] == "find":
        T.find_key(int(l[1]))
    if l[0] == "insert":
        T.insert_key(int(l[1]))
    if l[0] == "print":
        T.show_keys()
    if l[0] == "delete":
        T.delete_key(int(l[1]))

