from collections import deque
s = list(input())
S1 = deque()
S2 = deque()
sumA = 0
n = len(s)
for i in range(n):
    c = s[i]
    # バックスラッシュならS1に今の位置を積む
    if c == '\\':
        S1.append(i)
    # スラッシュでかつS1が空でなければ、
    elif c == '/' and len(S1) > 0:
        # S１から対応するバックスラッシュだった位置を取り出してjに
        j = S1.pop()
        # sumAに今の位置からJを引いた値を加算する
        sumA += i - j
        a = i - j
        while len(S2) > 0 and S2[len(S2)-1][0] > j:
            a += S2.pop()[1]
        S2.append([j,a])

print(sumA)
ans = list()
k = len(S2)
for i in range(len(S2)):
    ans.append(S2[i][1])
if len(ans) > 0:
    print(k," ".join(map(str, ans)))
else:
    print(k)