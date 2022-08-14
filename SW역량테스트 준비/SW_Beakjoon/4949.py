while True:
    st = input()
    if st == ".":
        break
    lst = []
    l_cnt = 0
    r_cnt = 0
    L_cnt = 0
    R_cnt = 0
    for i in st:
        if r_cnt > l_cnt:
            break
        elif i == "(" or i == ")" or i == "[" or i == "]":
            lst.append(i)
            if i == "(":
                l_cnt += 1
            elif i == ")":
                r_cnt += 1
            elif i == "[":
                L_cnt += 1
            elif i == "]":
                R_cnt += 1
    if len(lst) != 0:
        if lst[0] == lst[-1]:
            if l_cnt == r_cnt and L_cnt == R_cnt:
                print("yes")
            else:
                print("no")
        else:
            print("no")