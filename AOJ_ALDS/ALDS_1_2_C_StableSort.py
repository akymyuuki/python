n = int(input())
a = [x for x in input().split()]
b = a.copy()

def selectionSort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        if minj != i:
            a[i],a[minj] = a[minj],a[i]
    return a

def bubbleSort(a, n):
    flag = True
    while flag:
        flag = False
        for i in range(n-1, 0, -1):
            if a[i][1] < a[i-1][1]:
                a[i],a[i-1] = a[i-1],a[i]
                flag = True
    return a

bubbleSort(a, n)
print(" ".join(map(str, a)))
print("Stable")

selectionSort(b, n)
print(" ".join(map(str, b)))
if a == b:
    print("Stable")
else:
    print("Not stable")
