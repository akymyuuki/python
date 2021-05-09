line = input().split()
N = int(line[0])
K = int(line[1])

line = input().split()
nums = list(map(int, line))

# 雪だまを昇順に並べ替えておく
nums.sort()
l = 0
r = N-1
cnt = 0

while l < r:
    # Kより大きな雪だるまを作れるなら
    if ((nums[l] + nums[r]) >= K):
        # cntを増やす
        cnt += 1
        # 左端・右端の両方を内側に一つずつ縮める
        l += 1
        r -= 1

    # Kより大きい雪だるまを作れないなら
    else:
        # 左端を内側に縮めて、大きい雪玉を使用する
        l += 1

print(cnt)
