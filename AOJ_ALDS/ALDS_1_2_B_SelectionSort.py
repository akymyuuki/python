n = int(input())
a = list(map(int,input().split()))


def selectionSort(a, n):
    cnt = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if minj != i:
            cnt += 1
        a[i],a[minj] = a[minj],a[i]
    return a,cnt
    
b,cnt = selectionSort(a, n)
print(" ".join(map(str,b)))
print(cnt)
