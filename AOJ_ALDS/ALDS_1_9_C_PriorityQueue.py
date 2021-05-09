
import sys
A = [-1] * 4000001
H = 0
a = [None] * 2000000
h = 0

def max_heapify(idx):
    left_idx = idx * 2
    right_idx = left_idx + 1

    max_idx = idx

    if A[left_idx] > A[max_idx]:
        max_idx = left_idx
    if A[right_idx] > A[max_idx]:
        max_idx = right_idx

    if max_idx != idx:
        tmp = A[idx]
        A[idx] = A[max_idx]
        A[max_idx] = tmp
        max_heapify(max_idx)
    return


def insert(k):
    global H
    A[H+1] = k
    H += 1
    idx = H
    while idx > 1:
        parent_idx = idx // 2
        if A[idx] > A[parent_idx]:
            tmp = A[parent_idx]
            A[parent_idx] = A[idx]
            A[idx] = tmp
        else:
            break
        idx = parent_idx
    return


def extract():
    global h
    a[h] = A[1]
    h += 1
    global H
    A[1] = A[H]
    A[H] = -1
    H -= 1
    max_heapify(1)
    return


def main():
    commands = sys.stdin.readlines()
    for command in commands:
        if command[0] == 'i':
            insert(int(command[7:]))
        elif command[1] == 'x':
            extract()
        elif command[1] == 'n':
            break

    for i in range(h):
        print(a[i])
    return


main()