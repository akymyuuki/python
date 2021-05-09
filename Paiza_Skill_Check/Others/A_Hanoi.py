
def hanoi(n, f, t, work):
    if n > 0:
        hanoi(n - 1, f, work, t)
        # 手順を格納する
        _from.append(f)
        _to.append(t)
        hanoi(n-1, work, t, f)


# 解いた手順を格納するリスト
_from = list()
_to = list()

line = input().split()
n = int(line[0])
t = int(line[1])

# ハノイの塔を一度解く
hanoi(n, 0, 2, 1)

sticks = list()
for i in range(3):
    sticks.append(list())

for i in range(n):
    sticks[0].append(n-i)

# 格納した手順を最初から取り出し数値を移動させていく
for i in range(t):
    a = _from.pop(0)
    b = _to.pop(0)
    c = sticks[a].pop()
    sticks[b].append(c)

# スティックの表示
for i in range(3):
    if len(sticks[i]) == 0:
        print("-")
    else:
        ans = map(str, sticks[i])
        ans = ' '.join(ans)
        print(ans)
