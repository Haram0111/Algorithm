def OUTtimechange(time):
    hour, mit = time.split(":")
    return int(hour) * 60 + int(mit) + 10 #퇴실시간 + 청소시간

def INtimechange(time):
    hour, mit = time.split(":")
    return int(hour) * 60 + int(mit) #입실시간

def solution(book_time):
    answer = 0
    book_time.sort(key = lambda x : x[0])
    lst = [OUTtimechange(book_time[0][1])] #입실시간이 lst중에 제일 작은 것 보다 크다면 방 사용 가능
    for i in range(1,len(book_time)):
        if lst[0] <= INtimechange(book_time[i][0]):
            lst.pop(0)
            lst.append(OUTtimechange(book_time[i][1]))
        else: 
            lst.append(OUTtimechange(book_time[i][1]))
        lst.sort()
    return len(lst)
            