from collections import deque
a = list(input().split())
n = deque()
for i in range(len(a)):
    if a[i] == "+":
        x = n.pop()
        y = n.pop()
        n.append(x + y)
    elif a[i] == "-":
        x = n.pop()
        y = n.pop()
        n.append(y - x)
    elif a[i] == "*":
        x = n.pop()
        y = n.pop()
        n.append(x * y)
    else:
        n.append(int(a[i]))
print(n.pop())