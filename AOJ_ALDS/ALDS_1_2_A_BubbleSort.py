n = int(input())
a = list(map(int,input().split()))


def bubbleSort(a, n):
    cnt = 0
    flag = True
    while flag:
        flag = False
        for i in range(n-1, 0, -1):
            if a[i] < a[i-1]:
                a[i],a[i-1] = a[i-1],a[i]
                cnt += 1
                flag = True
    print(" ".join(map(str,a)))
    return cnt

cnt = bubbleSort(a, n)
print(cnt)
