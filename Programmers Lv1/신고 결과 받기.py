def solution(id_list, report, k):
    report = set(report) #중복제거
    report = list(report)
    result = [0 for i in range(len(id_list))] #결과
    answer = {}
    for i in range(len(id_list)):
        answer[id_list[i]] = []
    for i in report:
        a = i.split(" ") #a[0]가 a[1]을 신고했다. a[1] dictionary에 a[0]를 삽입한다.
        answer[a[1]].append(a[0])
    for i in id_list: #신고 수가 k 이상인 친구들을 찾는다.
        if len(answer[i]) >= k:
            for j in answer[i]: #신고한 사람들의 리스트
                for l in range(len(id_list)): #모든 사람의 list와 비교해서 몇번째 index인지 알기 위함이다.
                     if j == id_list[l]:
                        result[l] += 1
    return result
    
    #로직
    #frodo : [muzi, apeach] 2이상이고
    #frodo의 list안에 있는 사람들에게 메일이 전송 될 예정이다.
    #때문에 id_list를 담고 있는 2차원 배열도 있어야 할 것 같다.