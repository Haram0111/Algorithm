import heapq

def solution(scoville, K):
    cnt = 0
    scoville.sort()
    while(True):
        if scoville[0] >= K:
            break
        elif len(scoville) <= 1:
            return -1
        else:
            cnt += 1
            mini = heapq.heappop(scoville)
            mini2 = heapq.heappop(scoville)
            new = mini + mini2*2
            heapq.heappush(scoville, new)
    return cnt