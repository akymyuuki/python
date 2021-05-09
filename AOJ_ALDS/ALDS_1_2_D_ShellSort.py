n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
cnt = 0
G = list()

def insertionSort(a, n, g):
    global cnt
    for i in range(n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j+g] = a[j]
            j = j - g
            cnt += 1
        a[j+g] = v

def shellSort(a, n):
    h = 1
    while h <= n:
        G.append(h)
        h = 3*h+1
    G.reverse()
    for i in range(len(G)):
        insertionSort(a, n ,G[i])
    
    
shellSort(a, n)

print(len(G))
print(" ".join(map(str,G)))
print(cnt)
for i in range(n):
    print(a[i])