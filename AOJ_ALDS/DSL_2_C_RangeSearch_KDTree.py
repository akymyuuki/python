import math
from operator import itemgetter
from bisect import bisect_left, bisect_right

n = int(input())
XY = [tuple(map(int, input().split())) + (i, ) for i in range(n)]
XY.sort()
root = int(math.sqrt(n))

low = [x for x, y, id in XY[::root]]
high = [x for x, y, i in XY[root - 1::root]] + [float('inf')]

XY = [sorted(XY[i:i + root], key=itemgetter(1)) for i in range(0, n, root)]
XY = [([y for x, y, i in xyi], xyi) for xyi in XY]

Q = int(input())
for _ in range(Q):
    sx, tx, sy, ty = map(int, input().split())
    ret = []
    for i in range(bisect_left(high, sx), bisect_right(low, tx)):
        k, v = XY[i]
        for i in range(bisect_left(k, sy), bisect_right(k, ty)):
            if sx <= v[i][0] <= tx:
                ret.append(v[i][2])
    if ret:
        ret.sort()
        print('\n'.join(map(str,ret)))
    print()

