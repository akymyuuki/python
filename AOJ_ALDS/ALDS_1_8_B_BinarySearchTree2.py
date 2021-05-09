# 入力の高速化
import sys
input = sys.stdin.readline


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        if self.root == None:
            node = Node(key, parent, None, None)
            self.root = node
        else:
            node = Node(key, parent, None, None)
            cmp_node = self.root
            while True:
                if cmp_node.parent > parent and cmp_node.left == None:
                    cmp_node.left = node
                    break
                elif cmp_node.parent > parent and cmp_node.left != None:
                    cmp_node = cmp_node.left
                elif cmp_node.parent < parent and cmp_node.right == None:
                    cmp_node.right = node
                    break
                elif cmp_node.parent < parent and cmp_node.right != None:
                    cmp_node = cmp_node.right
    def find(self, node, k):
        while node != None:
            if node.key == int(k):
                return True
            if int(k) < node.key:
                node = node.left
            else:
                node = node.right
        return False
            

class Node:
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(" " + str(node.key), end="")
    inOrder(node.right)


def preOrder(node):
    if node == None:
        return
    print(" " + str(node.key), end="")
    preOrder(node.left)
    preOrder(node.right)


n = int(input())
T = BinarySearchTree()
# 入力は一度に行っておいた方が早い
Order = []
for i in range(n):
    l = input().split()
    Order.append(l)

for l in Order:
    if l[0] == "find":
        t = T.find(T.root, l[1])
        if t == True:
            print("yes")
        else:
            print("no")
    if l[0] == "insert":
        T.insert(int(l[1]), int(l[1]))
    if l[0] == "print":
        inOrder(T.root)
        print()
        preOrder(T.root)
        print()
