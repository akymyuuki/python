n, m = list(map(int, input().split()))
s = input()
# 事前に与えられた文字列に出現する文字の数をそれぞれカウント
G = s.count('G')
C = s.count('C')
P = s.count('P')

# グーの時には指の数に変化は出ないので、
# チョキとパーの組み合わせを事前に配列に格納しておく
c = list()
p = list()
for i in range(n+1):
    for j in range(n+1):
        if 2*i + 5*j == m and n - i - j >= 0:
            c.insert(len(c), i)
            p.insert(len(p), j)

ans = 0

# 格納した組み合わせが０になるまで繰り返す

while len(c) > 0:
    win = 0
    # 格納した配列からポップで取り出す
    cc = c.pop(0)
    pp = p.pop(0)

    # 取り出した組み合わせと対戦相手の手を比較して、勝利数を計算する
    # パーとグーの数を数えて、少ない方が結果的に勝利数となるので、
    # こちらが勝てる組み合わせで数の少ない方を勝利数にプラスする
    win += min(G, pp)
    win += min(P, cc)
    win += min(C, n - cc - pp)

    # 計算したwinとansを比較して大きい方をansに代入する
    # これによって一番勝利数が多い時を求められる
    ans = max(ans, win)

print(ans)
