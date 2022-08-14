lst = []
N = int(input())
for i in range(N):
    a = input()
    a = a.split(" ")
    if a[0] == "push":
        lst.append(a[1])
    elif a[0] == "pop":
        if len(lst) == 0:
            print("-1")
        else:  print(lst.pop())
    elif a[0] == "size":
        print(len(lst))
    elif a[0] == "empty":
        if len(lst) == 0:
            print("1")
        else: print("0")
    elif a[0] == "top":
        if len(lst) == 0:
            print("-1")
        else: print(lst[-1])