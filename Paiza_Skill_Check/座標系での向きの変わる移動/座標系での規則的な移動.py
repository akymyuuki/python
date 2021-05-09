'''
開始時点の x , y 座標と移動の歩数 N が与えられます。
以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。
なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。
'''

x, y, n = map(int, input().split())

#　ある方角に向かって進んだ時に変化するX Yの値
moveX = [0, 1, 0, -1]
moveY = [-1, 0, 1, 0]

d = 1  # 初期方角は東

# 問題の制限 -100 < x < 100　よりも大きなマップを宣言しておく
size = 300
map = [[0] * size for i in range(size)]

# マップの中央の値を1にする
gap = int(size / 2)
map[x + gap][y + gap] = 1

# n歩の移動を繰り返す
for i in range(n):
    x += moveX[d]
    y += moveY[d]
    # 移動した位置は1にして移動済みとする。gapをプラスする。
    map[x + gap][y + gap] = 1

    # 時計回りにぐるぐる回る = moveX,moveYを+1ずらして移動した場所が0ならその方向を向く　
    nextD = 0 if d + 1 == 4 else d + 1
    if map[x + moveX[nextD] + gap][y + moveY[nextD] + gap] == 0:
        d = 0 if d + 1 == 4 else d + 1

print(x, y)
