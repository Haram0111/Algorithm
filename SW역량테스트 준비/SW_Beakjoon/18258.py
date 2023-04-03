import sys
from collections import deque

lst = deque()
N = int(sys.stdin.readline())
for i in range(N):
    order = input()
    if order == 'pop':
        if len(lst) == 0:
            print(-1)
        else:  print(lst.popleft())
    elif order == 'size':
        print(len(lst))
    elif order == 'empty':
        if len(lst) == 0:
            print(1)
        else: print(0)
    elif order == 'front':
        if len(lst) == 0:
            print(-1)
        else: print(lst[0])
    elif order == 'back':
        if len(lst) == 0:
            print(-1)
        else: print(lst[-1])
    else:
        a = order.split()
        lst.append(a[1])