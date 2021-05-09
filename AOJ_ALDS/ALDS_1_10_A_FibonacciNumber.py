n = int(input())
A = [1 for i in range(50)]

for i in range(2, n+1):
    A[i] = (A[i-1] + A[i-2])
print (A[n])