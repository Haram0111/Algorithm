import sys
lst = []
N = int(sys.stdin.readline())
for i in range(N):
    a = sys.stdin.readline().split()
    order = a[0]
    if order == "push":
        lst.append(a[1])
    elif order == "pop":
        if len(lst) == 0:
            print(-1)
        else:  print(lst.pop())
    elif order == "size":
        print(len(lst))
    elif order == "empty":
        if len(lst) == 0:
            print(1)
        else: print(0)
    elif order == "top":
        if len(lst) == 0:
            print(-1)
        else: print(lst[-1])