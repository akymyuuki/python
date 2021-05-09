import copy
n = int(input())
A = list(map(int, input().split()))

def partition(p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
   
q = partition(0, n-1)
S = list(map(str,A))

for i in range(n):
    if i == q:
        S[i] = "["+S[i]+"]"

print(" ".join(S))