import math
d = int(input())

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def koch(d, a, b):
    if d == 0:
        return 
    s,t,u = Point(0,0),Point(0,0),Point(0,0)
    th = math.pi * 60 / 180
    
    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y
    
    koch(d - 1, a, s)
    print('{:.8f} {:.8f}'.format(s.x, s.y))
    koch(d - 1, s, u)
    print('{:.8f} {:.8f}'.format(u.x, u.y))
    koch(d - 1, u, t)
    print('{:.8f} {:.8f}'.format(t.x, t.y))
    koch(d - 1, t, b)

a,b = Point(0,0),Point(0,0)

a.x = 0
a.y = 0
b.x = 100
b.y = 0

print('{:.8f} {:.8f}'.format(a.x, a.y))
koch(d, a, b)
print('{:.8f} {:.8f}'.format(b.x, b.y))