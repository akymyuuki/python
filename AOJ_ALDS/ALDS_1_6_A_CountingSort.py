def CountingSort(A, B):

    C = [0 for i in range(max(A)+1)]

    # C[i] に i の出現数を記録する
    for i in range(0, len(A)):
        C[A[i]] += 1

    # C[i] に i 以下の数を記録する
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    for i in range(0, len(A)):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1


n = int(input())
A = list(map(int, input().split()))

B = [0 for i in range(n)]
CountingSort(A, B)

print(' '.join(map(str, B)))
