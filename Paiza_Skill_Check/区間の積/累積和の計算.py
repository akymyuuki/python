n = int(input())
arr = list(map(int, input().split()))

# それまでの計算結果を覚えておくための変数
ans = 0

for i in range(len(arr)):
    # 累積和はそれまでの計算結果 + 新しい数値
    ans += arr[i]
    print(ans)
