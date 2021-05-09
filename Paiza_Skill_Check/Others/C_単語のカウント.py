arr = list(input().split())

list = {}

for i in range(len(arr)):
    if arr[i] in list:
        list[arr[i]] += 1
    else:
        list[arr[i]] = 1

for k,v in list.items():
    print(k, v)