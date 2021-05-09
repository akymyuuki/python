n = int(input())

maxv = -99999999999
minv = int(input())

for i in range(n-1):
    r = int(input())
    maxv = max(maxv, r - minv)
    minv = min(minv, r)
    
print(maxv)