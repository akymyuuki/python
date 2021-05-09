import math
n = int(input())
A = list(map(int, input().split()))
cnt = 0

def mergeSort(A, left, right):
    if left+1 < right:
        mid = math.floor((left + right) / 2)
        cntL = mergeSort(A, left, mid)
        cntR = mergeSort(A, mid, right)
        return merge(A, left, mid, right) + cntL + cntR
    return 0

def merge(A, left,mid, right):
    n1 = mid - left
    n2 = right - mid
    cnt = 0
    L = A[left:mid] +[2000000000]
    R = A[mid:right]+[2000000000]

    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if(L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return cnt
    
ans = mergeSort(A, 0, n)

print(" ".join(map(str, A)))
print(ans)