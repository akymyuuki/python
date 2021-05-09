n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

def binarySearch(S,key):
    left = 0
    right = len(S)
    while left < right:
        mid = int((left + right) / 2)
        if key == S[mid]:
            return 1
        elif key < S[mid]:
            right = mid
        else:
            left = mid+1
    return 0

cnt = 0
for i in range(q):
    cnt += binarySearch(S, T[i])
print(cnt)