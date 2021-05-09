def maxHeapfy(i):
    l = 2 * i 
    r = 2 * i + 1
    # 左の子、自分、右の子で値が最大のノードを選ぶ
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeapfy(largest)


H = int(input())
A = [None] + list(map(int, input().split()))

for i in range(H//2, 0, -1):
   maxHeapfy(i)
A.pop(0)
print(' ' + ' '.join(map(str, A)))
