from functools import lru_cache
# 再帰メモ化のためのインポート

n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

# この問題はテキストと同じような書き方をしてもAcceptできなかった。
# Pythonの再帰自体の遅さに起因するのかもしれない。
# https://qiita.com/alchemist/items/c75174c41b0bcd31ecc6
# ↑の記事を参考にして再帰メモ化を設定したらAcceptできた。

# 再帰メモ設定 maxsizeは一応10000にしているがもう少し小さくしてもいいかもしれない
@lru_cache(maxsize=10000)
def solve(i, m):
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i + 1, m) or solve(i + 1, m - a[i])
    return res

for i in range(q):
    if solve(0,m[i]) == True:
        print("yes")
    else:
        print("no")