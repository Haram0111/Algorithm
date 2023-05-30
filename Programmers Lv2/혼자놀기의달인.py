def solution(cards):
    check = [False] * len(cards)
    lst = [0,0]
    #결국 loop라는 것에 초점을 둬야한다 어디서 시작해도 무조건 끝나게 되어있음
    for i in range(len(cards)):
        if False not in check:
            break
        if check[i] != False: #이미 루프에 속해있는거임
            #print(cards[i], "넘어감")
            continue
        else: #아직 안들른 곳이 있다면
            cnt = 1
            check[i] = True
            pre = cards[i] #index 0에 8이라는 값임
            while True: #여기서 루프를 만들어주는거임
                move_index = pre - 1 #move_index는 7임
                if check[move_index] == False: #이제 막 루프에 들어간거임
                    check[move_index] = True
                    cnt += 1
                    pre = cards[move_index]
                else:
                    break
            if cnt > lst[1]:
                lst[1] = cnt
            lst.sort(reverse=True)
    return lst[0] * lst[1]