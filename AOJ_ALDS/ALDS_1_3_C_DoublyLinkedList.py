from collections import deque
n = int(input())
Dlist = deque()

for i in range(n):
    c = input()
    if c == "deleteFirst":
        Dlist.popleft()
    elif c == "deleteLast":
        Dlist.pop()
    else:
        c,k = c.split()
        if c == "insert":
            Dlist.appendleft(k)
        elif c == "delete":
            try:
                Dlist.remove(k)    
            except:
                continue
print(" ".join(map(str, Dlist)))