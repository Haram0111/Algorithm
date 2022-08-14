N = int(input())
for i in range(N):
    a = input()
    L_cnt = 0
    R_cnt = 0
    if a[0] == ")" or a[len(a)-1] == "(":
        print("NO")
    else:
        for j in range(len(a)):            
            if R_cnt > L_cnt:
                break
            elif a[j] == "(":
                L_cnt += 1
            elif a[j] == ")":
                R_cnt += 1
        if L_cnt != R_cnt:
            print("NO")
        else:
            print("Yes")