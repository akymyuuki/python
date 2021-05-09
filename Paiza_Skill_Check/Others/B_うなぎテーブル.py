line = input().split()
n = int(line[0])
m = int(line[1])

table = [0] * n
ok = True

for i in range(m):
    ok = True
    line = input().split()
    a = int(line[0])
    b = int(line[1])

    # 席に座れるか確認する
    for j in range(a):
        c = j + b
        # 最大テーブル数を超えている場合、nを引いて範囲内に収める
        if c >= n:
            c -= n
        if table[c] == 1:
            ok = False

    # 席に座れるなら座らせる
    if ok == True:
        for j in range(a):
            c = j + b
            if c >= n:
                c -= n
            table[c] = 1

print(sum(table))
