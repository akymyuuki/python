
N = int(input())

line = input().split()
nums = list(map(int, line))
cnt = 0

for i in range(N):
    nums[i] -= 1

for i in range(N):
    a = nums[i]
    b = -1
    # 元の本の番号に帰ってくるまで交換を続ける
    while a != i:
        b = nums[a]
        nums[a] = a
        a = b
        cnt += 1
    nums[a] = a

print(cnt)
