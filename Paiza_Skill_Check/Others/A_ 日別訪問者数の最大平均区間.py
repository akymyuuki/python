n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
sum_a = list()
cnt = 0
index = 0

s = 0
for i in range(k):
    s += a[i]

sum_a.append(s)
max_a = s

for i in range(1, n-k+1):
    s -= a[i-1]
    s += a[i+k-1]
    sum_a.append(s)
    max_a = max(max_a, s)

for i in range(0, len(sum_a)):
    if sum_a[len(sum_a) - i - 1] == max_a:
        cnt += 1
        index = len(sum_a)-i

print(cnt, index)
