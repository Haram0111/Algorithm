N = int(input())
N_card = list(map(int,input().split(" ")))
M = int(input())
M_card = list(map(int,input().split(" ")))

for i in M_card:
    if i in N_card:
        print("1")
    else:
        print("0")