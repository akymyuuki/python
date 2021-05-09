from collections import deque
n,q = map(int, input().split())
queue = deque()
class process:
    def __init__(self,name,time):
        self.name = name
        self.time = time
        
for i in range(n):
    name,time = input().split()
    time = int(time)
    queue.append(process(name,time))

t = 0
while len(queue) > 0:
    a = queue.popleft()
    if a.time > q:
        a.time -= q
        t += q
        queue.append(a)
    else:
        t += a.time
        a.time = 0
        print(a.name,t)
        