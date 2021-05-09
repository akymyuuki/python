import math
def parent (i):
    return int(i / 2)

def left (i):
    return i * 2

def right (i):
    return i * 2 + 1

H = int(input())
A = list(map(int, input().split()))
A.insert(0, -1)
for i in range(1, H+1):
    print("node " + str(i) + ": key = " + str(A[i]) + ", " , end = "")
    if parent(i) >= 1:
        print("parent key = " + str(A[parent(i)]) + ", ", end = "")
    if left(i) <= H:
        print("left key = " + str(A[left(i)]) + ", ", end = "")
    if right(i) <= H:
        print("right key = " + str(A[right(i)]) + ", ", end = "")
    print()