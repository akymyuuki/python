n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

cnt = 0

# テキストに載っているWhile型のリニアサーチ
def linearSearch(S,key):
    a = 0
    b = len(S)
    while a < b:
        if S[a] == key:
            return 1
        a += 1
    return 0

for i in range(q):
    cnt += linearSearch(S,T[i])
print(cnt)