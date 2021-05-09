import copy
import math
n = int(input())
A = list()
[A.append(input().split()) for i in range(n)]
B = copy.copy(A)


def partition(p, r):
    x = int(A[r][1])
    i = p-1
    for j in range(p, r):
        y = int(A[j][1])
        if y <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
    
def quickSort(p,r):
    if p < r:
        q = partition(p, r)
        quickSort(p, q-1)
        quickSort(q+1, r)
        
quickSort(0,n-1)

def mergeSort(B,left, right):
    if left+1 < right:
        mid = math.floor((left + right) / 2)
        mergeSort(B, left, mid)
        mergeSort(B, mid, right)
        merge(B, left, mid, right)
    return 0

def merge(arr, left,mid, right):
    n1 = mid - left
    n2 = right - mid
    L = arr[left:mid] +[[" ",2000000000]]
    R = arr[mid:right]+[[" ",2000000000]]

    i = 0
    j = 0
    for k in range(left, right):
        if(int(L[i][1]) <= int(R[j][1])):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

mergeSort(B, 0, n)

if A == B:
    print("Stable")
else:
    print("Not stable")

for i in range(n):
    print(" ".join(A[i]))